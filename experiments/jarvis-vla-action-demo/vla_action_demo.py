"""Toy JARVIS-VLA-style action-interface demo.

The demo is rule-based. It illustrates how a VLA-style interface maps
observation, instruction, and state to a structured game action.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
ACTION_SPACE_PATH = ROOT / "action_space.json"
SCENES_PATH = ROOT / "demo_scenes.json"
LOG_PATH = ROOT / "logs" / "example_run.md"


def load_json(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise TypeError(f"{path} must contain a list")
    return data


def action_names(action_space: list[dict[str, Any]]) -> set[str]:
    return {action["name"] for action in action_space}


def candidate_actions(scene: dict[str, Any], available: set[str]) -> list[str]:
    state = scene["state"]
    visible = set(state["visible_objects"])
    instruction = scene["instruction"].lower()
    candidates = ["move_forward", "turn_left", "turn_right", "wait"]

    if visible & {"tree_trunk", "iron_ore", "zombie"}:
        candidates.append("attack")
    if visible & {"crafting_table", "furnace"}:
        candidates.append("use")
    if "craft" in instruction:
        candidates.append("craft_item")
    if "wooden_pickaxe" in state["inventory"]:
        candidates.append("equip_item")
    if "night" == state.get("time") or "survive" in instruction:
        candidates.extend(["retreat", "place_block"])

    return [action for action in candidates if action in available]


def select_action(scene: dict[str, Any]) -> dict[str, Any]:
    state = scene["state"]
    inventory = set(state["inventory"])
    visible = set(state["visible_objects"])
    instruction = scene["instruction"].lower()

    if "survive" in instruction and "zombie" in visible:
        return {
            "action": "retreat",
            "arguments": {"threat": "zombie"},
            "confidence": 0.88,
            "explanation": "Immediate survival requires increasing distance before building or fighting.",
        }

    if "iron" in instruction and "iron_ore" in visible and "wooden_pickaxe" in inventory:
        return {
            "action": "equip_item",
            "arguments": {"item": "stone_pickaxe_or_better"},
            "confidence": 0.82,
            "explanation": "Mining iron with a wooden pickaxe would fail, so the next action is to switch or obtain a valid tool.",
        }

    if "smelt" in instruction and "furnace" in visible:
        return {
            "action": "use",
            "arguments": {"target": "furnace"},
            "confidence": 0.91,
            "explanation": "The furnace is visible and the inventory contains iron ore and fuel.",
        }

    if "craft" in instruction and "crafting_table" in visible:
        return {
            "action": "use",
            "arguments": {"target": "crafting_table"},
            "confidence": 0.86,
            "explanation": "The crafting table is the correct interface before selecting planks or sticks.",
        }

    if "wood" in instruction and "tree_trunk" in visible:
        return {
            "action": "attack",
            "arguments": {"target": "tree_trunk"},
            "confidence": 0.9,
            "explanation": "The tree trunk is centered and collecting wood maps to an attack/mine action.",
        }

    return {
        "action": "wait",
        "arguments": {},
        "confidence": 0.4,
        "explanation": "No safe grounded action was identified from the toy rules.",
    }


def planning_gap(scene: dict[str, Any]) -> str:
    gaps = {
        "tree_collect_wood": "A high-level plan says collect wood, but the controller still needs a grounded attack action on the trunk.",
        "craft_table_planks": "A language plan may say craft sticks, but action prediction must choose the crafting table interaction first.",
        "furnace_smelt_iron": "A plan says smelt iron, but the next low-level action is use furnace, not mine or craft.",
        "iron_wooden_pickaxe": "A plan might say mine iron, but action prediction must reject an invalid tool/action pair.",
        "night_mob_survive": "A plan says survive, but immediate control should prioritize retreat or defense based on the visible threat.",
    }
    return gaps[scene["id"]]


def vla_difference(scene: dict[str, Any]) -> str:
    differences = {
        "tree_collect_wood": "VLA prediction binds the instruction to the visible trunk and emits an executable attack action.",
        "craft_table_planks": "VLA prediction chooses an interaction with the visible station before recipe selection.",
        "furnace_smelt_iron": "VLA prediction maps visual furnace evidence and inventory state to the use action.",
        "iron_wooden_pickaxe": "VLA prediction can encode action preconditions and avoid executing a doomed mining action.",
        "night_mob_survive": "VLA prediction reacts to visual threat state rather than only following a long-horizon plan.",
    }
    return differences[scene["id"]]


def render_scene(scene: dict[str, Any], candidates: list[str], selected: dict[str, Any]) -> str:
    lines = [
        f"## {scene['id']}",
        "",
        f"- Observation: {scene['observation']}",
        f"- Instruction: {scene['instruction']}",
        "",
        "### Relevant State",
        "",
        "```json",
        json.dumps(scene["state"], indent=2, sort_keys=True),
        "```",
        "",
        "### Candidate Actions",
        "",
        ", ".join(f"`{action}`" for action in candidates),
        "",
        "### Selected Action",
        "",
        "```json",
        json.dumps(selected, indent=2, sort_keys=True),
        "```",
        "",
        "### Explanation",
        "",
        selected["explanation"],
        "",
        "### Why Pure Language Planning Is Insufficient",
        "",
        planning_gap(scene),
        "",
        "### How VLA-Style Action Prediction Differs",
        "",
        vla_difference(scene),
        "",
    ]
    return "\n".join(lines)


def build_log(scenes: list[dict[str, Any]], action_space: list[dict[str, Any]]) -> str:
    available = action_names(action_space)
    sections = [
        "# Example Run",
        "",
        "This log was generated by `vla_action_demo.py`.",
        "It is a toy JARVIS-VLA-style action-interface demo, not official model inference.",
        "",
    ]
    for scene in scenes:
        sections.append(render_scene(scene, candidate_actions(scene, available), select_action(scene)))
    return "\n".join(sections).rstrip() + "\n"


def main() -> int:
    action_space = load_json(ACTION_SPACE_PATH)
    scenes = load_json(SCENES_PATH)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(build_log(scenes, action_space), encoding="utf-8")
    print(f"wrote {LOG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
