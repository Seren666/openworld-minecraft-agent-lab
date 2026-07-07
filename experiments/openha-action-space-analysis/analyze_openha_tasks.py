#!/usr/bin/env python3
"""Rule-based OpenHA/CrossAgent action-space taxonomy analysis.

This script reads public task metadata from a local OpenHA checkout or zip
snapshot when available, then falls back to a bounded representative sample.
It does not run Minecraft, train models, download datasets, or evaluate any
official checkpoints.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


TASK_LIST_REL = "CrossAgent/STRL/data_processor/utils/task_list.json"
TASK_SUC_RATE_REL = "CrossAgent/STRL/data_processor/task_suc_rate.json"
ACTION_DIST_REL = "CrossAgent/STRL/scripts/action_dist/action_dist.json"


MANUAL_REPRESENTATIVE_TASKS = [
    "obtain iron ingot",
    "craft stone sword",
    "build a small shelter",
    "obtain diamond",
    "smelt iron",
    "fight hostile mob",
    "explore cave",
    "use furnace",
]


COMPLEX_ITEMS = {
    "beacon",
    "brewing_stand",
    "enchanting_table",
    "end_crystal",
    "ender_chest",
    "ender_eye",
    "netherite_scrap",
    "netherite_ingot",
    "netherite_pickaxe",
    "diamond",
    "diamond_pickaxe",
    "diamond_sword",
    "shulker_box",
    "sea_lantern",
    "conduit",
    "elytra",
    "totem_of_undying",
}

COOKING_TERMS = {
    "smelt",
    "furnace",
    "cooked",
    "baked",
    "dried",
    "charcoal",
    "glass",
    "brick",
    "iron_ingot",
    "gold_ingot",
    "copper_ingot",
    "netherite_scrap",
}

BUILDING_TERMS = {
    "shelter",
    "house",
    "wall",
    "door",
    "fence",
    "slab",
    "stairs",
    "planks",
    "roof",
    "bridge",
    "bed",
}

INTERACTION_TERMS = {
    "use",
    "interact",
    "furnace",
    "crafting_table",
    "chest",
    "button",
    "lever",
    "door",
    "anvil",
    "brewing_stand",
}

NAVIGATION_TERMS = {"explore", "cave", "find", "locate", "travel", "navigate"}

COMBAT_TERMS = {
    "kill",
    "fight",
    "hostile",
    "zombie",
    "skeleton",
    "creeper",
    "spider",
    "slime",
    "golem",
    "mob",
    "enderman",
    "vindicator",
}

TOOL_TERMS = {
    "ore",
    "diamond",
    "iron",
    "gold",
    "redstone",
    "lapis",
    "obsidian",
    "stone",
    "deepslate",
    "ancient_debris",
}

SIMPLE_MINE_TERMS = {
    "dirt",
    "sand",
    "gravel",
    "grass",
    "grass_block",
    "oak_log",
    "birch_log",
    "acacia_log",
    "spruce_log",
    "jungle_log",
    "dark_oak_log",
    "oak_leaves",
    "birch_leaves",
    "hay_block",
    "sugar_cane",
    "flower",
    "tulip",
}


@dataclass(frozen=True)
class TaskRecord:
    task_name: str
    source: str


class OpenHASource:
    def __init__(self, path: Path | None):
        self.path = path
        self.kind = "none"
        self.zip_file: zipfile.ZipFile | None = None
        self.root_prefix = ""
        if path and path.exists():
            if path.is_dir():
                self.kind = "directory"
            elif path.suffix.lower() == ".zip":
                self.kind = "zip"
                self.zip_file = zipfile.ZipFile(path)
                names = self.zip_file.namelist()
                if names and "/" in names[0]:
                    self.root_prefix = names[0].split("/")[0] + "/"

    def close(self) -> None:
        if self.zip_file:
            self.zip_file.close()

    def exists(self, rel: str) -> bool:
        if self.kind == "directory" and self.path:
            return (self.path / rel).exists()
        if self.kind == "zip" and self.zip_file:
            return self.root_prefix + rel in self.zip_file.namelist()
        return False

    def read_text(self, rel: str) -> str | None:
        if self.kind == "directory" and self.path:
            p = self.path / rel
            if p.exists():
                return p.read_text(encoding="utf-8", errors="replace")
        if self.kind == "zip" and self.zip_file:
            name = self.root_prefix + rel
            if name in self.zip_file.namelist():
                return self.zip_file.read(name).decode("utf-8", errors="replace")
        return None

    def list_files(self) -> list[str]:
        if self.kind == "directory" and self.path:
            return [
                str(p.relative_to(self.path)).replace("\\", "/")
                for p in self.path.rglob("*")
                if p.is_file()
            ]
        if self.kind == "zip" and self.zip_file:
            return [
                n[len(self.root_prefix) :]
                for n in self.zip_file.namelist()
                if n.startswith(self.root_prefix) and not n.endswith("/")
            ]
        return []


def find_openha_source(arg_path: str | None) -> OpenHASource:
    candidates: list[Path] = []
    if arg_path:
        candidates.append(Path(arg_path))
    for env_name in ("OPENHA_REPO", "OPENHA_ZIP"):
        val = os.environ.get(env_name)
        if val:
            candidates.append(Path(val))
        candidates.extend(
            [
                Path("/root/autodl-tmp/external_repos/OpenHA"),
                Path("/root/autodl-tmp/external_repos/OpenHA-main.zip"),
            ]
        )
    for c in candidates:
        src = OpenHASource(c)
        if src.kind != "none":
            return src
    return OpenHASource(None)


def normalize_task_name(name: str) -> str:
    return re.sub(r"\s+", " ", name.strip().replace("-", "_")).lower()


def add_task(tasks: dict[str, TaskRecord], name: str, source: str) -> None:
    clean = normalize_task_name(name)
    if not clean:
        return
    if clean not in tasks:
        tasks[clean] = TaskRecord(task_name=clean, source=source)
    elif source not in tasks[clean].source:
        tasks[clean] = TaskRecord(
            task_name=clean, source=f"{tasks[clean].source}; {source}"
        )


def load_tasks(src: OpenHASource) -> tuple[list[TaskRecord], dict[str, object]]:
    tasks: dict[str, TaskRecord] = {}
    metadata: dict[str, object] = {
        "source_kind": src.kind,
        "source_path": str(src.path) if src.path else "not_found",
        "task_list_count": 0,
        "task_suc_rate_model_count": 0,
        "task_suc_rate_task_count": 0,
        "rollout_debug_task_count": 0,
        "task_family_files": [],
        "action_dist_available": False,
        "crossagent_folders": [],
    }
    files = src.list_files()
    metadata["file_count"] = len(files)
    metadata["crossagent_folders"] = sorted(
        {
            f.split("/")[1]
            for f in files
            if f.startswith("CrossAgent/") and len(f.split("/")) > 2
        }
    )

    task_list_text = src.read_text(TASK_LIST_REL)
    if task_list_text:
        task_list = json.loads(task_list_text)
        metadata["task_list_count"] = len(task_list)
        for task in task_list:
            add_task(tasks, task, TASK_LIST_REL)

    suc_rate_text = src.read_text(TASK_SUC_RATE_REL)
    if suc_rate_text:
        suc = json.loads(suc_rate_text)
        metadata["task_suc_rate_model_count"] = len(suc)
        suc_tasks = set()
        for model_tasks in suc.values():
            if isinstance(model_tasks, dict):
                suc_tasks.update(model_tasks.keys())
        metadata["task_suc_rate_task_count"] = len(suc_tasks)
        for task in suc_tasks:
            add_task(tasks, task, TASK_SUC_RATE_REL)

    action_dist_text = src.read_text(ACTION_DIST_REL)
    metadata["action_dist_available"] = bool(action_dist_text)
    if action_dist_text:
        try:
            action_dist = json.loads(action_dist_text)
            metadata["action_dist_models"] = list(action_dist.keys())
            action_types = set()
            for model_data in action_dist.values():
                if isinstance(model_data, dict):
                    action_types.update(model_data.keys())
            metadata["action_dist_task_family_keys"] = sorted(action_types)
        except json.JSONDecodeError:
            metadata["action_dist_parse_error"] = True

    rollout_tasks = set()
    for f in files:
        if "/rollout_debug/" not in f:
            continue
        match = re.search(r"reset_\d+_([^/]+)/", f)
        if match:
            rollout_tasks.add(match.group(1))
    metadata["rollout_debug_task_count"] = len(rollout_tasks)
    for task in rollout_tasks:
        add_task(tasks, task, "rollout_debug directory names")

    family_files = [
        f
        for f in files
        if f.startswith("openagents/envs/tasks/") and f.endswith(".py")
    ]
    metadata["task_family_files"] = family_files

    for task in MANUAL_REPRESENTATIVE_TASKS:
        add_task(tasks, task, "manual_representative_sample")

    if not tasks:
        for task in MANUAL_REPRESENTATIVE_TASKS:
            add_task(tasks, task, "manual_fallback_sample")

    return sorted(tasks.values(), key=lambda r: r.task_name), metadata


def target_part(task_name: str) -> str:
    if ":" in task_name:
        return task_name.split(":", 1)[1]
    return task_name


def has_any(text: str, terms: Iterable[str]) -> bool:
    return any(t in text for t in terms)


def classify_task(task_name: str) -> dict[str, object]:
    name = normalize_task_name(task_name)
    target = target_part(name)
    text = f"{name} {target}"

    category = "mixed_or_unknown"
    if name.startswith("kill_entity") or has_any(text, COMBAT_TERMS):
        category = "combat"
    elif has_any(text, NAVIGATION_TERMS):
        category = "navigation_or_exploration"
    elif "shelter" in text or "build" in text or has_any(text, BUILDING_TERMS):
        category = "building_or_shelter"
    elif name.startswith("mine_block"):
        category = "mining"
    elif name.startswith("interact_block") or has_any(text, INTERACTION_TERMS):
        category = "tool_use_or_interaction"
    elif name.startswith("smelt_item") or has_any(text, COOKING_TERMS):
        category = "smelting_or_cooking"
    elif name.startswith("craft_item") or name.startswith("craft item") or "craft " in text:
        category = "crafting"
    elif name.startswith("drop:"):
        category = "tool_use_or_interaction"
    elif "obtain" in text or target in COMPLEX_ITEMS:
        category = "long_horizon_obtain"

    if (
        "obtain" in text
        or target in COMPLEX_ITEMS
        or ("diamond" in text and "block" not in text)
        or "netherite" in text
        or "beacon" in text
    ):
        category = "long_horizon_obtain"
    if "smelt" in text or "cooked" in text or "baked" in text or "furnace" in text:
        if category not in {"long_horizon_obtain", "building_or_shelter"}:
            category = "smelting_or_cooking"

    interfaces: list[str]
    info_types: list[str]
    failure: str
    notes: str

    if category == "crafting":
        interfaces = [
            "high_level_planning",
            "memory_or_prerequisite_reasoning",
            "mid_level_skill_action",
        ]
        info_types = ["recipe_or_prerequisite", "inventory_or_tool_state"]
        failure = "prerequisite_memory_missing"
        notes = "Crafting tasks depend on recipe structure, inventory state, and a correct crafting interface."
    elif category == "smelting_or_cooking":
        interfaces = [
            "high_level_planning",
            "memory_or_prerequisite_reasoning",
            "mid_level_skill_action",
            "visual_grounding_or_mask_action",
            "dynamic_action_space_switching",
        ]
        info_types = [
            "recipe_or_prerequisite",
            "inventory_or_tool_state",
            "visual_target_localization",
        ]
        failure = "visual_prompt_insufficient_for_planning"
        notes = "Smelting/cooking combines recipe, fuel, station use, and visible furnace/campfire interaction."
    elif category == "mining":
        interfaces = [
            "visual_grounding_or_mask_action",
            "low_level_control",
            "mid_level_skill_action",
        ]
        info_types = [
            "visual_target_localization",
            "low_level_reactive_control",
        ]
        if has_any(text, TOOL_TERMS) and not has_any(target, SIMPLE_MINE_TERMS):
            interfaces.extend(
                ["memory_or_prerequisite_reasoning", "dynamic_action_space_switching"]
            )
            info_types.append("inventory_or_tool_state")
            failure = "prerequisite_memory_missing"
        else:
            failure = "language_only_target_ambiguous"
        notes = "Mining needs target localization, tool validity, and low-level interaction with the block."
    elif category == "combat":
        interfaces = [
            "visual_grounding_or_mask_action",
            "low_level_control",
            "dynamic_action_space_switching",
        ]
        info_types = [
            "visual_target_localization",
            "low_level_reactive_control",
            "navigation_or_exploration_state",
        ]
        failure = "dynamic_switching_needed"
        notes = "Combat requires reactive control, target tracking, and switching between approach, attack, and retreat."
    elif category == "navigation_or_exploration":
        interfaces = [
            "high_level_planning",
            "visual_grounding_or_mask_action",
            "low_level_control",
            "dynamic_action_space_switching",
        ]
        info_types = ["navigation_or_exploration_state", "visual_target_localization"]
        failure = "low_level_sequence_too_long"
        notes = "Exploration needs high-level route intent plus low-level movement and visual hazard handling."
    elif category == "building_or_shelter":
        interfaces = [
            "high_level_planning",
            "memory_or_prerequisite_reasoning",
            "mid_level_skill_action",
            "visual_grounding_or_mask_action",
            "low_level_control",
            "dynamic_action_space_switching",
        ]
        info_types = [
            "long_horizon_planning",
            "inventory_or_tool_state",
            "visual_target_localization",
            "low_level_reactive_control",
        ]
        failure = "mid_level_skill_missing_parameter"
        notes = "Building/shelter tasks require layout planning, material state, placement geometry, and local control."
    elif category == "long_horizon_obtain":
        interfaces = [
            "high_level_planning",
            "memory_or_prerequisite_reasoning",
            "mid_level_skill_action",
            "visual_grounding_or_mask_action",
            "low_level_control",
            "dynamic_action_space_switching",
        ]
        info_types = [
            "long_horizon_planning",
            "recipe_or_prerequisite",
            "inventory_or_tool_state",
            "memory_or_failure_trace",
            "mixed",
        ]
        failure = "dynamic_switching_needed"
        notes = "Long-horizon obtain tasks span prerequisites, search, crafting, tool use, and execution."
    elif category == "tool_use_or_interaction":
        interfaces = [
            "memory_or_prerequisite_reasoning",
            "mid_level_skill_action",
        ]
        info_types = ["inventory_or_tool_state", "visual_target_localization"]
        if not name.startswith("drop:"):
            interfaces.append("visual_grounding_or_mask_action")
        if has_any(text, INTERACTION_TERMS) or target in COMPLEX_ITEMS:
            interfaces.append("dynamic_action_space_switching")
            failure = "mid_level_skill_missing_parameter"
            notes = "Interaction tasks depend on selecting the correct object and passing the right action parameters."
        else:
            failure = "high_level_action_infeasible"
            notes = "Inventory/drop-style tasks mainly need inventory state and a valid mid-level command."
    else:
        interfaces = [
            "high_level_planning",
            "memory_or_prerequisite_reasoning",
            "dynamic_action_space_switching",
        ]
        info_types = ["mixed"]
        failure = "mixed"
        notes = "Task name does not reveal enough structure; classification is deliberately cautious."

    if category in {"crafting", "smelting_or_cooking"} and target in COMPLEX_ITEMS:
        if "low_level_control" not in interfaces:
            interfaces.append("low_level_control")
        if "long_horizon_planning" not in info_types:
            info_types.append("long_horizon_planning")
        if "memory_or_failure_trace" not in info_types:
            info_types.append("memory_or_failure_trace")
        failure = "dynamic_switching_needed"
        notes += " The target appears complex enough to require multi-stage action-space switching."

    return {
        "category": category,
        "preferred_interfaces": interfaces,
        "required_information_type": info_types,
        "likely_failure_under_fixed_action_space": failure,
        "notes": notes,
    }


def pct(count: int, total: int) -> str:
    if total == 0:
        return "0.0"
    return f"{count * 100.0 / total:.1f}"


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def summarize(rows: list[dict[str, object]], key: str) -> list[dict[str, object]]:
    total = len(rows)
    counts = Counter(row[key] for row in rows)
    return [
        {
            key: label,
            "task_count": count,
            "percentage_of_tasks": pct(count, total),
        }
        for label, count in counts.most_common()
    ]


def summarize_interfaces(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    total = len(rows)
    counts: Counter[str] = Counter()
    for row in rows:
        for label in str(row["preferred_interfaces"]).split(";"):
            counts[label] += 1
    return [
        {
            "preferred_interface": label,
            "task_count": count,
            "percentage_of_tasks": pct(count, total),
        }
        for label, count in counts.most_common()
    ]


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(c, "")) for c in columns) + " |")
    return "\n".join(lines)


def write_metadata_report(
    path: Path,
    metadata: dict[str, object],
    rows: list[dict[str, object]],
) -> None:
    source_kind = metadata.get("source_kind")
    source_counts = Counter(str(row["source"]) for row in rows)
    unique_task_names = len({str(row["task_name"]) for row in rows})
    task_list_rows = sum(1 for row in rows if TASK_LIST_REL in str(row["source"]))
    suc_rate_rows = sum(1 for row in rows if TASK_SUC_RATE_REL in str(row["source"]))
    rollout_rows = sum(1 for row in rows if "rollout_debug directory names" in str(row["source"]))
    manual_rows = source_counts.get("manual_representative_sample", 0)
    task_list_only = source_counts.get(TASK_LIST_REL, 0)
    suc_rate_only = source_counts.get(TASK_SUC_RATE_REL, 0)
    rollout_only = source_counts.get("rollout_debug directory names", 0)
    text = f"""# Metadata Source Report

This report documents the source used for the OpenHA/CrossAgent action-space taxonomy analysis.

This is not the official OpenHA benchmark size. The OpenHA/CrossAgent papers describe the benchmark scope as over 800 distinct Minecraft tasks. This local artifact contains task-name records parsed from public metadata/config files plus bounded representative additions.

## Source Location

| Field | Value |
| --- | --- |
| OpenHA repository URL | https://github.com/CraftJarvis/OpenHA |
| Branch | `main` |
| Commit hash | `606efc69e945bd02c700e584136bcc105d22f122` |
| Local source kind | `{source_kind}` |
| Local source storage | external repository or snapshot inspected outside this project repository |
| Analysis scope | exploratory metadata/config-derived task-name records plus bounded representative additions |

## Directory Structure Summary

- Root README and package metadata are available in the OpenHA snapshot.
- `CrossAgent/` is present.
- CrossAgent subfolders observed: `{", ".join(metadata.get("crossagent_folders", []))}`.
- Minecraft-related task family files observed: `{", ".join(metadata.get("task_family_files", []))}`.
- `openagents/assets/recipes/` is present in the snapshot, but raw recipe files are not copied into this repository.

## Source Breakdown

| Source path | Source type | Raw unique names found | Final rows mentioning source | Exclusive new rows after exact-name de-duplication | Entry interpretation |
| --- | --- | ---: | ---: | ---: | --- |
| `CrossAgent/STRL/data_processor/task_suc_rate.json` | CrossAgent metadata/config summary | {metadata.get("task_suc_rate_task_count", 0)} | {suc_rate_rows} | {suc_rate_only} | task-name records / atomic or config-level task variants, not the official benchmark-size denominator |
| `CrossAgent/STRL/data_processor/utils/task_list.json` | CrossAgent task-list/config file | {metadata.get("task_list_count", 0)} | {task_list_rows} | {task_list_only} | task-list entries that overlap with `task_suc_rate.json` in this snapshot |
| rollout-debug directory names | generated/debug directory labels | {metadata.get("rollout_debug_task_count", 0)} | {rollout_rows} | {rollout_only} | directory-derived task labels that overlap with config metadata; not new benchmark tasks |
| `manual_representative_sample` | manually added analysis sample | {len(MANUAL_REPRESENTATIVE_TASKS)} | {manual_rows} | {manual_rows} | bounded Minecraft examples added only to cover readable task types such as shelter, cave exploration, and furnace use |

## Final Row-Source Combinations

| Final `source` value in `task_taxonomy.csv` | Row count |
| --- | ---: |
| `{TASK_SUC_RATE_REL}` | {source_counts.get(TASK_SUC_RATE_REL, 0)} |
| `{TASK_LIST_REL}; {TASK_SUC_RATE_REL}` | {source_counts.get(f"{TASK_LIST_REL}; {TASK_SUC_RATE_REL}", 0)} |
| `{TASK_LIST_REL}; {TASK_SUC_RATE_REL}; rollout_debug directory names` | {source_counts.get(f"{TASK_LIST_REL}; {TASK_SUC_RATE_REL}; rollout_debug directory names", 0)} |
| `manual_representative_sample` | {manual_rows} |

## Final CSV Accounting

| Statistic | Count |
| --- | ---: |
| Rows in `task_taxonomy.csv` | {len(rows)} |
| Unique task names in `task_taxonomy.csv` | {unique_task_names} |
| Duplicate exact task names in final CSV | {len(rows) - unique_task_names} |

The final CSV de-duplicates exact task names. Upstream sources overlap conceptually and by exact name, so source counts should not be added together as an official benchmark count.

## Metadata Type

The strongest local source is structured JSON task metadata from the public OpenHA/CrossAgent repository snapshot. The taxonomy uses task names and public summary/config metadata only. It does not copy raw external repository code, raw rollout logs, model weights, datasets, checkpoints, or videos into this project repository.

## Limitations

- Task names do not fully reveal trajectory difficulty, visual state, inventory state, or world layout.
- `task_suc_rate.json` appears to be public aggregate task-level metadata/config output, not an official evaluation run performed in this repository.
- The 1200 local records are not the official OpenHA/CrossAgent benchmark size.
- The taxonomy is rule-based and preliminary.
- Representative tasks are added only to cover shelter, cave exploration, furnace use, and other task types not visible in the structured task-name list.
"""
    path.write_text(text, encoding="utf-8")


def write_failure_modes(path: Path) -> None:
    tasks = [
        (
            "obtain iron ingot",
            [
                "All high-level actions may jump to `mine iron ore` without checking pickaxe tier, furnace, and fuel prerequisites.",
                "All mid-level skill actions can call useful skills, but may fail if the wrong tool, ore target, or furnace parameters are supplied.",
                "All low-level controls are executable, but the prerequisite chain becomes too long and credit assignment becomes weak.",
                "Language-only actions under-specify which ore, tree, fuel source, or furnace should be used.",
                "Visual/mask actions can identify ore or furnace targets but cannot alone plan the full smelting chain.",
                "Dynamic switching uses high-level planning for prerequisites, memory for tool/fuel constraints, visual grounding for ore/furnace targets, and low-level control for mining interaction.",
            ],
        ),
        (
            "craft stone sword",
            [
                "All high-level actions may request `craft sword` before collecting cobblestone, sticks, or a crafting table.",
                "All mid-level skill actions work only if recipe and inventory parameters are correct.",
                "All low-level controls make the GUI and collection sequence unnecessarily long.",
                "Language-only actions may omit exact inventory slots or station state.",
                "Visual/mask actions help locate a crafting table or slot but do not infer the recipe chain by themselves.",
                "Dynamic switching combines recipe memory, mid-level crafting, and low-level GUI correction.",
            ],
        ),
        (
            "build a small shelter",
            [
                "All high-level actions may say `build shelter` without specifying footprint, material, door placement, or threat response.",
                "All mid-level skill actions can place blocks but may miss geometry and safety constraints.",
                "All low-level controls are possible but slow and brittle over many placements.",
                "Language-only actions lose spatial layout and obstacle details.",
                "Visual/mask actions help with placement targets but cannot decide the whole shelter plan.",
                "Dynamic switching uses high-level layout planning, inventory checks, visual placement, and low-level correction.",
            ],
        ),
        (
            "obtain diamond",
            [
                "All high-level actions may choose `mine diamond` despite missing iron pickaxe, cave access, or safety preparation.",
                "All mid-level skill actions depend on valid tool and target parameters.",
                "All low-level controls make the search/mining chain too long for reliable control.",
                "Language-only actions do not identify ore blocks or hazards.",
                "Visual/mask actions can ground diamond ore but cannot guarantee prerequisite tool planning.",
                "Dynamic switching links prerequisite memory, exploration, ore grounding, and precise mining control.",
            ],
        ),
        (
            "smelt iron",
            [
                "All high-level actions may skip checking ore, furnace, and fuel.",
                "All mid-level skill actions may fail if furnace/fuel/ore parameters are missing.",
                "All low-level controls over GUI slots are fragile without inventory-state reasoning.",
                "Language-only actions do not identify the actual furnace or inventory slots.",
                "Visual/mask actions help select furnace and slots but do not plan fuel acquisition.",
                "Dynamic switching combines prerequisite reasoning, station grounding, and low-level GUI execution.",
            ],
        ),
        (
            "fight hostile mob",
            [
                "All high-level actions may say `attack` without reacting to distance, health, terrain, or multiple enemies.",
                "All mid-level skill actions may lack parameters for timing, aim, retreat, or shield use.",
                "All low-level controls can react, but without high-level policy may chase bad fights.",
                "Language-only actions miss exact mob position and motion.",
                "Visual/mask actions are useful for target tracking but not enough for survival policy.",
                "Dynamic switching alternates between target grounding, low-level combat control, and high-level retreat/equip decisions.",
            ],
        ),
        (
            "explore cave",
            [
                "All high-level actions may under-specify route, lighting, hazard avoidance, and return path.",
                "All mid-level skill actions may not adapt to local cave geometry.",
                "All low-level controls are executable but inefficient over long exploration horizons.",
                "Language-only actions lose spatial and hazard detail.",
                "Visual/mask actions help detect openings, ores, and threats but do not maintain exploration memory.",
                "Dynamic switching uses high-level exploration goals, visual hazard detection, memory of visited areas, and low-level movement.",
            ],
        ),
        (
            "use furnace",
            [
                "All high-level actions may assume a furnace exists and is reachable.",
                "All mid-level skill actions need exact object, fuel, and ingredient parameters.",
                "All low-level controls are brittle around GUI opening and slot placement.",
                "Language-only actions do not distinguish furnace from crafting table or chest.",
                "Visual/mask actions help choose the furnace but do not infer smelting prerequisites.",
                "Dynamic switching grounds the furnace visually, checks inventory prerequisites, and executes GUI actions at low level.",
            ],
        ),
    ]
    lines = [
        "# Example Failure Modes",
        "",
        "This is a qualitative, Minecraft-aware analysis. It is not an official OpenHA/CrossAgent evaluation.",
        "",
    ]
    for task, bullets in tasks:
        lines.append(f"## Task: {task}")
        lines.append("")
        labels = [
            "All high-level actions",
            "All mid-level skill actions",
            "All low-level controls",
            "Language-only actions",
            "Visual/mask actions",
            "Dynamic action-space switching",
        ]
        for label, bullet in zip(labels, bullets):
            lines.append(f"- **{label}:** {bullet}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_key_findings(
    path: Path,
    rows: list[dict[str, object]],
    category_rows: list[dict[str, object]],
    interface_rows: list[dict[str, object]],
) -> None:
    total = len(rows)
    unique_task_names = len({str(row["task_name"]) for row in rows})
    cat = {r["category"]: r for r in category_rows}
    iface = {r["preferred_interface"]: r for r in interface_rows}
    manual_rows = sum(1 for row in rows if row["source"] == "manual_representative_sample")
    lines = [
        "# Key Findings",
        "",
        "This is a preliminary, exploratory taxonomy over OpenHA/CrossAgent public metadata/config-derived task-name records plus a bounded representative sample. It is not official model evaluation.",
        "",
        "The OpenHA/CrossAgent paper framing describes an over-800-task benchmark. The 1200 records here are local unique task-name records parsed from public metadata/config outputs plus bounded additions, not the official benchmark size.",
        "",
        "## Strongest Findings",
        "",
        f"1. **The local artifact contains {total} task-name rows and {unique_task_names} unique task names.** This should be read as an exploratory metadata/config scope, not as the official OpenHA benchmark denominator.",
        f"2. **Most records come from CrossAgent metadata/config outputs.** The final CSV includes {manual_rows} bounded representative samples; the remaining records are parsed from public OpenHA/CrossAgent files.",
        "3. **The taxonomy suggests that Minecraft task families place different pressure on action granularity.** Crafting and smelting lean toward prerequisite/inventory reasoning, while mining, combat, building, and navigation lean more toward visual grounding or low-level control.",
        "4. **Dynamic action-space switching appears as a meaningful subset rather than a universal requirement.** This supports asking when to switch action interfaces, not only which next action to predict.",
        "",
        "## Detailed Exploratory Statistics",
        "",
    ]
    for label in ["crafting", "mining", "tool_use_or_interaction", "combat", "smelting_or_cooking", "long_horizon_obtain"]:
        if label in cat:
            r = cat[label]
            lines.append(
                f"- `{label}` accounts for {r['task_count']} local records ({r['percentage_of_tasks']}% of rows)."
            )
            break
    for label in ["dynamic_action_space_switching", "memory_or_prerequisite_reasoning", "visual_grounding_or_mask_action", "low_level_control"]:
        if label in iface:
            r = iface[label]
            lines.append(
                f"- `{label}` is assigned to {r['task_count']} local records ({r['percentage_of_tasks']}% of rows)."
            )
            break
    if "memory_or_prerequisite_reasoning" in iface:
        r = iface["memory_or_prerequisite_reasoning"]
        lines.append(
            f"- `memory_or_prerequisite_reasoning` appears in {r['task_count']} local records ({r['percentage_of_tasks']}% of rows)."
        )
    if "visual_grounding_or_mask_action" in iface:
        r = iface["visual_grounding_or_mask_action"]
        lines.append(
            f"- `visual_grounding_or_mask_action` appears in {r['task_count']} local records ({r['percentage_of_tasks']}% of rows)."
        )

    lines.extend(
        [
            "",
            "Percentages are computed over local task-name rows. In this artifact, row-level and unique-task percentages are identical because the final CSV has no duplicate exact task names.",
            "",
            "## Manual Sanity Check",
            "",
            "- A 100-record stratified sample is provided in `manual_check_sample_100.csv`.",
            "- The sample uses first-pass conservative manual labels and confidence notes.",
            "- This is a qualitative sanity check, not a validation result.",
            "- Agreement is not reported because labels were not adjudicated by independent annotators and no trajectory-level ground truth was used.",
            "",
            "## Cautious Hypotheses",
            "",
            "- Long-horizon obtain tasks may benefit from memory-conditioned action-space selection.",
            "- Crafting and smelting tasks appear more dependent on prerequisite and inventory state than on raw low-level control alone.",
            "- Mining, combat, navigation, and building tasks appear more dependent on visual grounding and low-level control than recipe-only tasks.",
            "",
            "## Limitations",
            "",
            "- The taxonomy is rule-based and preliminary.",
            "- Task names and public metadata may not reveal full trajectory difficulty.",
            "- No official OpenHA/CrossAgent checkpoint inference or Minecraft evaluation was run.",
            "- The 1200 local task-name records are not the official over-800-task benchmark size reported in the paper framing.",
            "- The representative additions are bounded and are used only to cover task types missing from structured metadata.",
            "",
            "## Possible Future Directions",
            "",
            "- Memory-conditioned action-space selection.",
            "- Task-stage-aware action cost for GRPO.",
            "- Failure-trace-conditioned replanning.",
            "- Visual-grounding-aware low-level switching.",
            "- World-model-assisted action rollout analysis.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def evenly_select(rows: list[dict[str, object]], limit: int) -> list[dict[str, object]]:
    if len(rows) <= limit:
        return rows
    if limit <= 1:
        return rows[:limit]
    selected: list[dict[str, object]] = []
    used: set[int] = set()
    step = (len(rows) - 1) / (limit - 1)
    for i in range(limit):
        idx = round(i * step)
        while idx in used and idx + 1 < len(rows):
            idx += 1
        if idx in used:
            idx = next(j for j in range(len(rows)) if j not in used)
        used.add(idx)
        selected.append(rows[idx])
    return selected


def first_pass_manual_category(task_name: str, predicted_category: str) -> str:
    name = normalize_task_name(task_name)
    if name.startswith("craft_item") or name.startswith("craft item") or "craft " in name:
        return "crafting"
    if name.startswith("smelt_item") or "smelt" in name or "furnace" in name:
        return "smelting_or_cooking"
    if name.startswith("mine_block"):
        return "mining"
    if name.startswith("kill_entity") or has_any(name, COMBAT_TERMS):
        return "combat"
    if name.startswith("interact_block") or name.startswith("drop:") or name.startswith("use "):
        return "tool_use_or_interaction"
    if "explore" in name or "cave" in name:
        return "navigation_or_exploration"
    if "shelter" in name or name.startswith("build "):
        return "building_or_shelter"
    if "obtain" in name:
        return "long_horizon_obtain"
    return predicted_category


def first_pass_manual_interfaces(category: str, task_name: str) -> str:
    name = normalize_task_name(task_name)
    if category == "crafting":
        labels = [
            "high_level_planning",
            "memory_or_prerequisite_reasoning",
            "mid_level_skill_action",
        ]
        if target_part(name) in COMPLEX_ITEMS:
            labels.append("dynamic_action_space_switching")
        return ";".join(labels)
    if category == "smelting_or_cooking":
        return ";".join(
            [
                "high_level_planning",
                "memory_or_prerequisite_reasoning",
                "mid_level_skill_action",
                "visual_grounding_or_mask_action",
                "dynamic_action_space_switching",
            ]
        )
    if category == "mining":
        labels = [
            "mid_level_skill_action",
            "visual_grounding_or_mask_action",
            "low_level_control",
        ]
        if has_any(name, TOOL_TERMS):
            labels.append("memory_or_prerequisite_reasoning")
        return ";".join(labels)
    if category == "combat":
        return ";".join(
            [
                "visual_grounding_or_mask_action",
                "low_level_control",
                "dynamic_action_space_switching",
            ]
        )
    if category == "navigation_or_exploration":
        return ";".join(
            [
                "high_level_planning",
                "visual_grounding_or_mask_action",
                "low_level_control",
                "dynamic_action_space_switching",
            ]
        )
    if category == "building_or_shelter":
        return ";".join(
            [
                "high_level_planning",
                "memory_or_prerequisite_reasoning",
                "mid_level_skill_action",
                "visual_grounding_or_mask_action",
                "low_level_control",
                "dynamic_action_space_switching",
            ]
        )
    if category == "long_horizon_obtain":
        return ";".join(
            [
                "high_level_planning",
                "memory_or_prerequisite_reasoning",
                "mid_level_skill_action",
                "visual_grounding_or_mask_action",
                "low_level_control",
                "dynamic_action_space_switching",
            ]
        )
    return "high_level_planning;memory_or_prerequisite_reasoning"


def manual_confidence_and_note(
    task_name: str,
    source: str,
    predicted_category: str,
    manual_category: str,
) -> tuple[str, str]:
    name = normalize_task_name(task_name)
    if manual_category != predicted_category:
        return (
            "medium",
            "First-pass label differs from the rule prediction because the task prefix suggests a more conservative category; needs trajectory-level review.",
        )
    if source == "manual_representative_sample":
        return (
            "high",
            "Representative sample task is human-readable and directly supports the first-pass label.",
        )
    if (
        name.startswith("craft_item")
        or name.startswith("mine_block")
        or name.startswith("smelt_item")
        or name.startswith("kill_entity")
        or name.startswith("interact_block")
        or name.startswith("drop:")
    ):
        return (
            "high",
            "Task prefix and target object support the first-pass category; trajectory details are still not checked.",
        )
    if predicted_category == "mixed_or_unknown":
        return (
            "low",
            "Task name alone is ambiguous; requires benchmark definition or trajectory trace.",
        )
    return (
        "medium",
        "Plausible from task name, but missing inventory, visual state, and trajectory context.",
    )


def write_manual_check_sample(path: Path, rows: list[dict[str, object]]) -> None:
    targets = {
        "mining": 20,
        "tool_use_or_interaction": 17,
        "crafting": 17,
        "building_or_shelter": 16,
        "smelting_or_cooking": 10,
        "combat": 10,
        "long_horizon_obtain": 8,
        "navigation_or_exploration": 1,
        "mixed_or_unknown": 1,
    }
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["category"])].append(row)
    selected: list[dict[str, object]] = []
    selected_names: set[str] = set()
    for category, limit in targets.items():
        candidates = sorted(grouped.get(category, []), key=lambda r: str(r["task_name"]))
        for row in evenly_select(candidates, limit):
            selected.append(row)
            selected_names.add(str(row["task_name"]))
    if len(selected) < 100:
        for row in sorted(rows, key=lambda r: str(r["task_name"])):
            if str(row["task_name"]) in selected_names:
                continue
            selected.append(row)
            selected_names.add(str(row["task_name"]))
            if len(selected) == 100:
                break
    selected = selected[:100]

    out_rows = []
    for row in selected:
        task_name = str(row["task_name"])
        predicted_category = str(row["category"])
        manual_category = first_pass_manual_category(task_name, predicted_category)
        confidence, notes = manual_confidence_and_note(
            task_name,
            str(row["source"]),
            predicted_category,
            manual_category,
        )
        out_rows.append(
            {
                "task_name": task_name,
                "source": row["source"],
                "predicted_category": predicted_category,
                "predicted_interfaces": row["preferred_interfaces"],
                "required_information_type": row["required_information_type"],
                "likely_failure_under_fixed_action_space": row[
                    "likely_failure_under_fixed_action_space"
                ],
                "manual_category": manual_category,
                "manual_interfaces": first_pass_manual_interfaces(manual_category, task_name),
                "confidence": confidence,
                "notes": notes,
            }
        )
    write_csv(
        path,
        out_rows,
        [
            "task_name",
            "source",
            "predicted_category",
            "predicted_interfaces",
            "required_information_type",
            "likely_failure_under_fixed_action_space",
            "manual_category",
            "manual_interfaces",
            "confidence",
            "notes",
        ],
    )


def write_manual_check_protocol(path: Path) -> None:
    text = """# Manual Sanity-Check Protocol

This protocol documents the first-pass sanity check for the OpenHA/CrossAgent action-space taxonomy. It is a qualitative check, not an official validation result.

## Sample

- File: `manual_check_sample_100.csv`
- Size: 100 task records
- Sampling: deterministic stratified sample across predicted categories, with rare categories retained when available.
- Source: `task_taxonomy.csv`

## Labeling Rules

- `manual_category` uses conservative task-name interpretation. When task prefixes such as `craft_item`, `mine_block`, `smelt_item`, `kill_entity`, `interact_block`, or `drop:` are present, the prefix is prioritized over item semantics.
- `manual_interfaces` lists the action interfaces that appear necessary from the task name alone.
- `confidence` is `high` when the task verb/prefix clearly supports the first-pass label, `medium` when the task name is plausible but missing trajectory context, and `low` when the task name is too ambiguous for reliable labeling.
- `notes` explain whether the first-pass label agrees with the rule prediction or needs trajectory-level review.

## What This Check Does Not Claim

- It does not validate the taxonomy against official OpenHA/CrossAgent labels.
- It does not use simulator rollouts, trajectories, model outputs, or checkpoint inference.
- It does not report agreement as a benchmark metric.
- It does not change the official over-800-task benchmark framing from the papers.

## Next Step

A stronger validation pass would use benchmark task definitions or summarized trajectories and would compute category/interface agreement after independent annotation.
"""
    path.write_text(text, encoding="utf-8")


def write_resume_bullet(path: Path, total: int, metadata_count: int) -> None:
    lines = [
        "# Resume Bullet Drafts",
        "",
        "## Version A: Local Metadata-Derived Task Analysis",
        "",
        f"- Built an exploratory OpenHA/CrossAgent action-space taxonomy over {total} local task-name records parsed from public metadata/config files and bounded representative samples, quantifying how task types may depend on high-level planning, memory/prerequisite reasoning, visual grounding, low-level control, and dynamic action-space switching.",
        "",
        "## Version B: Bounded Sample Framing",
        "",
        f"- Built a lightweight OpenHA/CrossAgent action-space taxonomy over local metadata/config-derived records, comparing crafting, smelting, mining, combat, navigation, building, and long-horizon obtain task types across planning, memory, visual grounding, low-level control, and dynamic switching requirements without treating the local count as the official benchmark size.",
        "",
        "## 中文版本",
        "",
        f"- 基于 OpenHA/CrossAgent 公开 metadata/config task-name records 与少量代表性 Minecraft 样本，构建探索性的 action-space taxonomy，分析不同任务类型对 high-level planning、memory/prerequisite reasoning、visual grounding、low-level control 与 dynamic action-space switching 的依赖；该本地记录数不作为官方 benchmark 规模。",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--openha-source", default=None, help="Path to OpenHA dir or zip")
    parser.add_argument(
        "--out-dir",
        default=str(Path(__file__).resolve().parent / "results"),
        help="Output directory for CSV/Markdown summaries",
    )
    args = parser.parse_args()

    src = find_openha_source(args.openha_source)
    try:
        tasks, metadata = load_tasks(src)
    finally:
        src.close()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent

    rows: list[dict[str, object]] = []
    for record in tasks:
        cls = classify_task(record.task_name)
        rows.append(
            {
                "task_name": record.task_name,
                "source": record.source,
                "category": cls["category"],
                "preferred_interfaces": ";".join(cls["preferred_interfaces"]),
                "required_information_type": ";".join(cls["required_information_type"]),
                "likely_failure_under_fixed_action_space": cls[
                    "likely_failure_under_fixed_action_space"
                ],
                "notes": cls["notes"],
            }
        )

    category_rows = summarize(rows, "category")
    interface_rows = summarize_interfaces(rows)

    write_csv(
        out_dir / "task_taxonomy.csv",
        rows,
        [
            "task_name",
            "source",
            "category",
            "preferred_interfaces",
            "required_information_type",
            "likely_failure_under_fixed_action_space",
            "notes",
        ],
    )
    write_csv(
        out_dir / "category_summary.csv",
        category_rows,
        ["category", "task_count", "percentage_of_tasks"],
    )
    write_csv(
        out_dir / "action_space_summary.csv",
        interface_rows,
        ["preferred_interface", "task_count", "percentage_of_tasks"],
    )
    write_metadata_report(root / "metadata_source_report.md", metadata, rows)
    write_failure_modes(out_dir / "example_failure_modes.md")
    write_key_findings(out_dir / "key_findings.md", rows, category_rows, interface_rows)
    write_manual_check_sample(out_dir / "manual_check_sample_100.csv", rows)
    write_manual_check_protocol(out_dir / "manual_check_protocol.md")
    write_resume_bullet(
        out_dir / "resume_bullet.md",
        len(rows),
        int(metadata.get("task_suc_rate_task_count", 0) or 0),
    )

    print(f"source_kind={metadata.get('source_kind')}")
    print(f"source_path={metadata.get('source_path')}")
    print(f"tasks_analyzed={len(rows)}")
    print("category_summary")
    print(markdown_table(category_rows, ["category", "task_count", "percentage_of_tasks"]))
    print("action_space_summary")
    print(
        markdown_table(
            interface_rows,
            ["preferred_interface", "task_count", "percentage_of_tasks"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
