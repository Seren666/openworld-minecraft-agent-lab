"""Toy visual-temporal context prompting demo inspired by ROCKET-1.

This script uses only Python's standard library. It creates synthetic grid
scenes, mask overlays, small SVG assets, and a Markdown run log.
"""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
SCENES_PATH = ROOT / "demo_scenes.json"
ASSETS_DIR = ROOT / "assets"
LOG_PATH = ROOT / "logs" / "example_run.md"

CELL = 54
PADDING = 28


def load_scenes() -> list[dict[str, Any]]:
    with SCENES_PATH.open("r", encoding="utf-8") as file:
        scenes = json.load(file)
    if not isinstance(scenes, list):
        raise TypeError("demo_scenes.json must contain a list")
    return scenes


def object_at(scene: dict[str, Any], x: int, y: int) -> dict[str, Any] | None:
    for obj in scene["objects"]:
        if [x, y] in obj["cells"]:
            return obj
    return None


def mask_cells(scene: dict[str, Any]) -> set[tuple[int, int]]:
    return {tuple(cell) for cell in scene["mask_prompt"]["cells"]}


def previous_mask_cells(scene: dict[str, Any]) -> set[tuple[int, int]]:
    previous = scene.get("previous_mask")
    if not previous:
        return set()
    return {tuple(cell) for cell in previous["cells"]}


def render_ascii(scene: dict[str, Any]) -> str:
    width, height = scene["grid_size"]
    target = mask_cells(scene)
    previous = previous_mask_cells(scene)
    lines: list[str] = []

    for y in range(height):
        row: list[str] = []
        for x in range(width):
            obj = object_at(scene, x, y)
            char = obj["label"] if obj else "."
            if (x, y) in target:
                row.append(f"[{char}]")
            elif (x, y) in previous:
                row.append(f"({char})")
            else:
                row.append(f" {char} ")
        lines.append("".join(row).rstrip())
    return "\n".join(lines)


def svg_rect(x: int, y: int, fill: str, stroke: str = "#d0d4dc", width: int = 1) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{width}" />'
    )


def render_svg(scene: dict[str, Any], path: Path) -> None:
    width, height = scene["grid_size"]
    svg_width = width * CELL + PADDING * 2
    svg_height = height * CELL + PADDING * 2 + 42
    target = mask_cells(scene)
    previous = previous_mask_cells(scene)
    title = html.escape(scene["title"])

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">',
        '<rect width="100%" height="100%" fill="#f7f8fb" />',
        f'<text x="{PADDING}" y="24" font-family="Arial, sans-serif" font-size="16" font-weight="700" fill="#20242a">{title}</text>',
    ]

    for y in range(height):
        for x in range(width):
            px = PADDING + x * CELL
            py = PADDING + 18 + y * CELL
            obj = object_at(scene, x, y)
            fill = obj["color"] if obj else "#ffffff"
            parts.append(svg_rect(px, py, fill))
            if obj:
                parts.append(
                    f'<text x="{px + CELL / 2}" y="{py + CELL / 2 + 6}" '
                    'text-anchor="middle" font-family="Arial, sans-serif" '
                    'font-size="18" font-weight="700" fill="#111827">'
                    f'{html.escape(obj["label"])}</text>'
                )
            if (x, y) in previous:
                parts.append(
                    f'<rect x="{px + 5}" y="{py + 5}" width="{CELL - 10}" height="{CELL - 10}" '
                    'fill="none" stroke="#f59e0b" stroke-width="4" stroke-dasharray="6 5" />'
                )
            if (x, y) in target:
                parts.append(
                    f'<rect x="{px + 4}" y="{py + 4}" width="{CELL - 8}" height="{CELL - 8}" '
                    'fill="rgba(239,68,68,0.18)" stroke="#ef4444" stroke-width="5" />'
                )

    legend_y = PADDING + 18 + height * CELL + 26
    parts.extend(
        [
            f'<rect x="{PADDING}" y="{legend_y - 14}" width="18" height="18" fill="rgba(239,68,68,0.18)" stroke="#ef4444" stroke-width="4" />',
            f'<text x="{PADDING + 26}" y="{legend_y}" font-family="Arial, sans-serif" font-size="13" fill="#374151">current target mask</text>',
            f'<rect x="{PADDING + 176}" y="{legend_y - 14}" width="18" height="18" fill="none" stroke="#f59e0b" stroke-width="3" stroke-dasharray="5 4" />',
            f'<text x="{PADDING + 202}" y="{legend_y}" font-family="Arial, sans-serif" font-size="13" fill="#374151">previous mask when present</text>',
            "</svg>",
        ]
    )

    path.write_text("\n".join(parts), encoding="utf-8")


def render_scene_log(scene: dict[str, Any], svg_name: str) -> str:
    mask = scene["mask_prompt"]
    lines = [
        f"## {scene['title']}",
        "",
        f"- Scenario id: `{scene['id']}`",
        f"- Language-only instruction: {scene['language_instruction']}",
        f"- Ambiguity or failure risk: {scene['ambiguity']}",
        f"- Interaction type: `{mask['interaction']}`",
        f"- ROCKET-style object id: `{mask['obj_id']}`",
        f"- Mask target: `{mask['target']}` at cells `{mask['cells']}`",
        f"- Temporal context: {scene['temporal_context']}",
        "",
        "### ASCII Scene",
        "",
        "Legend: `[X]` is the current mask; `(X)` is a previous mask.",
        "",
        "```text",
        render_ascii(scene),
        "```",
        "",
        "### Visual Prompt Asset",
        "",
        f"![{scene['id']}](../assets/{svg_name})",
        "",
        "### Why Visual-Temporal Context Helps",
        "",
        scene["why_visual_prompt_helps"],
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    scenes = load_scenes()
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    sections = [
        "# Example Run",
        "",
        "This log was generated by `visual_prompt_demo.py` using synthetic scenes.",
        "It is a lightweight ROCKET-1-style visual prompt demo, not official inference.",
        "",
    ]

    for scene in scenes:
        svg_name = f"{scene['id']}.svg"
        render_svg(scene, ASSETS_DIR / svg_name)
        sections.append(render_scene_log(scene, svg_name))

    LOG_PATH.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {LOG_PATH}")
    print(f"wrote {len(scenes)} SVG assets to {ASSETS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
