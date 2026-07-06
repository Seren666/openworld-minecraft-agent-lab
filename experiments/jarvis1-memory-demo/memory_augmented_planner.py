"""Toy JARVIS-1-style memory-augmented Minecraft planner.

This is an original lightweight demo. It does not use official JARVIS-1 model
weights, raw memory entries, or a Minecraft simulator.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
MEMORY_PATH = ROOT / "demo_memory.json"
TASK_PATH = ROOT / "demo_tasks.json"
LOG_PATH = ROOT / "logs" / "example_run.md"

STOPWORDS = {
    "a",
    "an",
    "and",
    "before",
    "for",
    "if",
    "in",
    "is",
    "of",
    "or",
    "the",
    "to",
    "with",
}


def load_json(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise TypeError(f"Expected a list in {path}")
    return data


def tokens(value: Any) -> set[str]:
    text = json.dumps(value, sort_keys=True) if not isinstance(value, str) else value
    text = text.replace("_", " ")
    return {
        token
        for token in re.findall(r"[a-z0-9_]+", text.lower())
        if token not in STOPWORDS and len(token) > 1
    }


def state_value_tokens(value: Any) -> set[str]:
    if isinstance(value, dict):
        result: set[str] = set()
        for nested in value.values():
            result |= state_value_tokens(nested)
        return result
    if isinstance(value, list):
        result = set()
        for nested in value:
            result |= state_value_tokens(nested)
        return result
    return tokens(value)


def retrieve_memories(
    task: dict[str, Any],
    memories: list[dict[str, Any]],
    top_k: int = 3,
    min_score: int = 2,
) -> list[dict[str, Any]]:
    query_tokens = tokens(task.get("task", "")) | state_value_tokens(
        task.get("current_state", {})
    )
    scored: list[tuple[int, dict[str, Any]]] = []

    for memory in memories:
        memory_tokens = tokens(memory.get("task_cues", [])) | tokens(memory.get("memory", ""))
        score = len(query_tokens & memory_tokens)
        if score >= min_score:
            scored.append((score, memory))

    scored.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [memory for _, memory in scored[:top_k]]


def baseline_plan(task_name: str) -> list[str]:
    plans = {
        "obtain iron ingot": [
            "Find iron ore.",
            "Mine iron ore.",
            "Smelt the ore into an iron ingot.",
        ],
        "craft stone sword": [
            "Collect stone.",
            "Craft a stone sword.",
        ],
        "build a small shelter": [
            "Collect nearby blocks.",
            "Place walls and a roof.",
            "Stay inside when night begins.",
        ],
        "obtain diamond with insufficient tools": [
            "Find diamond ore.",
            "Mine the diamond ore.",
        ],
    }
    return plans.get(task_name, ["Break the task into resource, crafting, and execution steps."])


def memory_plan(task_name: str, retrieved: list[dict[str, Any]]) -> list[str]:
    plans = {
        "obtain iron ingot": [
            "Confirm wood, crafting table, and sticks.",
            "Mine cobblestone and craft a stone pickaxe.",
            "Mine iron ore with the stone pickaxe.",
            "Mine or collect fuel.",
            "Craft or use a furnace and smelt iron ore into an ingot.",
        ],
        "craft stone sword": [
            "Confirm access to a crafting table.",
            "Collect cobblestone with a pickaxe.",
            "Craft or keep two sticks.",
            "Use cobblestone and sticks at the crafting table to craft a stone sword.",
        ],
        "build a small shelter": [
            "Check time and mob risk first.",
            "Select flat ground near resources.",
            "Place compact walls, a roof, and a safe entrance.",
            "Add light if available and remain inside through night.",
        ],
        "obtain diamond with insufficient tools": [
            "Do not mine diamond ore with the current stone pickaxe.",
            "Obtain iron ore using a stone pickaxe.",
            "Smelt iron ore with fuel in a furnace.",
            "Craft an iron pickaxe.",
            "Return to diamond ore and mine it with the iron pickaxe.",
        ],
    }

    selected = plans.get(task_name, baseline_plan(task_name))
    if not retrieved:
        return selected

    memory_notes = [f"Use memory: {memory['implication']}" for memory in retrieved]
    return memory_notes + selected


def improvement(task_name: str) -> str:
    improvements = {
        "obtain iron ingot": (
            "Memory adds missing tool-level, furnace, and fuel constraints that the "
            "baseline plan omits."
        ),
        "craft stone sword": (
            "Memory adds the concrete recipe prerequisites: cobblestone, sticks, "
            "and crafting table."
        ),
        "build a small shelter": (
            "Memory makes the plan time-sensitive and prioritizes safety before night."
        ),
        "obtain diamond with insufficient tools": (
            "Memory prevents a destructive tool mismatch by requiring an iron pickaxe first."
        ),
    }
    return improvements.get(task_name, "Memory adds reusable constraints from similar tasks.")


def missing_memory_failure(task_name: str) -> str:
    failures = {
        "obtain iron ingot": "The agent may mine iron with a wooden pickaxe or forget fuel.",
        "craft stone sword": "The agent may try to craft without enough cobblestone or sticks.",
        "build a small shelter": "The agent may keep gathering until hostile mobs appear.",
        "obtain diamond with insufficient tools": "The agent may break diamond ore with a stone pickaxe and lose the resource.",
    }
    return failures.get(task_name, "The plan may omit hidden prerequisites.")


def irrelevant_memory_failure(task_name: str) -> str:
    failures = {
        "obtain iron ingot": "A shelter memory could waste daylight before collecting ore.",
        "craft stone sword": "A smelting memory could add an unnecessary furnace step.",
        "build a small shelter": "A diamond-tool memory could distract from immediate safety.",
        "obtain diamond with insufficient tools": "A sword recipe memory could add combat preparation without solving the tool-level blocker.",
    }
    return failures.get(task_name, "Irrelevant memory can add wrong subgoals.")


def render_task(task: dict[str, Any], retrieved: list[dict[str, Any]]) -> str:
    task_name = task["task"]
    lines = [
        f"## {task_name}",
        "",
        "### Current State",
        "",
        "```json",
        json.dumps(task["current_state"], indent=2, sort_keys=True),
        "```",
        "",
        "### Retrieved Memories",
        "",
    ]

    for index, memory in enumerate(retrieved, start=1):
        lines.append(
            f"{index}. `{memory['id']}`: {memory['memory']} Implication: {memory['implication']}"
        )

    lines.extend(["", "### Plan Without Memory", ""])
    lines.extend(f"{index}. {step}" for index, step in enumerate(baseline_plan(task_name), start=1))

    lines.extend(["", "### Plan With Memory", ""])
    lines.extend(
        f"{index}. {step}" for index, step in enumerate(memory_plan(task_name, retrieved), start=1)
    )

    lines.extend(
        [
            "",
            "### Explanation Of Improvement",
            "",
            improvement(task_name),
            "",
            "### Possible Failure If Memory Is Missing",
            "",
            missing_memory_failure(task_name),
            "",
            "### Possible Failure If Irrelevant Memory Is Retrieved",
            "",
            irrelevant_memory_failure(task_name),
            "",
        ]
    )
    return "\n".join(lines)


def build_log(tasks: list[dict[str, Any]], memories: list[dict[str, Any]]) -> str:
    sections = [
        "# Example Run",
        "",
        "This log was generated by `memory_augmented_planner.py` using toy memory entries.",
        "It is a lightweight JARVIS-1-style planning demo, not an official reproduction.",
        "",
    ]

    for task in tasks:
        sections.append(render_task(task, retrieve_memories(task, memories)))

    return "\n".join(sections).rstrip() + "\n"


def main() -> int:
    memories = load_json(MEMORY_PATH)
    tasks = load_json(TASK_PATH)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(build_log(tasks, memories), encoding="utf-8")
    print(f"wrote {LOG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
