"""Safely summarize the external JARVIS-1 memory file.

The script prints aggregate statistics only. It does not copy the source JSON,
dump raw memory entries, or write outputs by default.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from statistics import mean
from typing import Any


DEFAULT_MEMORY_PATH = Path(
    "/root/autodl-tmp/external_repos/JARVIS-1/jarvis/assets/memory.json"
)


def load_memory(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def iter_entries(data: Any) -> list[Any]:
    if isinstance(data, dict):
        return list(data.values())
    if isinstance(data, list):
        return data
    raise TypeError(f"Unsupported top-level JSON type: {type(data).__name__}")


def summarize(data: Any) -> dict[str, Any]:
    entries = iter_entries(data)
    entry_fields: Counter[str] = Counter()
    step_fields: Counter[str] = Counter()
    step_types: Counter[str] = Counter()
    plan_lengths: list[int] = []

    for entry in entries:
        if not isinstance(entry, dict):
            continue

        entry_fields.update(entry.keys())
        plan = entry.get("plan")
        if not isinstance(plan, list):
            continue

        plan_lengths.append(len(plan))
        for step in plan:
            if not isinstance(step, dict):
                continue
            step_fields.update(step.keys())
            step_type = step.get("type")
            if isinstance(step_type, str):
                step_types[step_type] += 1

    return {
        "top_level_type": type(data).__name__,
        "entry_count": len(entries),
        "entry_fields": entry_fields,
        "entries_with_plan": len(plan_lengths),
        "plan_lengths": plan_lengths,
        "step_fields": step_fields,
        "step_types": step_types,
    }


def print_summary(summary: dict[str, Any]) -> None:
    plan_lengths = summary["plan_lengths"]
    total_steps = sum(plan_lengths)

    print("JARVIS-1 fixed-memory aggregate summary")
    print("=" * 45)
    print(f"top_level_type: {summary['top_level_type']}")
    print(f"entry_count: {summary['entry_count']}")
    print(f"entries_with_plan: {summary['entries_with_plan']}")
    print(f"total_plan_steps: {total_steps}")

    if plan_lengths:
        print(
            "plan_length_min_max_avg: "
            f"{min(plan_lengths)} / {max(plan_lengths)} / {mean(plan_lengths):.2f}"
        )

    print("\nentry_fields:")
    for field, count in summary["entry_fields"].most_common():
        print(f"  {field}: {count}")

    print("\nstep_fields:")
    for field, count in summary["step_fields"].most_common():
        print(f"  {field}: {count}")

    print("\nstep_types:")
    for step_type, count in summary["step_types"].most_common():
        print(f"  {step_type}: {count}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print aggregate-only stats for the external JARVIS-1 memory file."
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_MEMORY_PATH,
        help="Path to external JARVIS-1 memory.json.",
    )
    args = parser.parse_args()

    if not args.path.exists():
        parser.error(f"memory file not found: {args.path}")

    data = load_memory(args.path)
    print_summary(summarize(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
