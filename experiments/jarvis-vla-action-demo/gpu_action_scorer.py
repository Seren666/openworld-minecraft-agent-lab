"""Tiny GPU-backed toy action scorer for the JARVIS-VLA action demo.

This is infrastructure evidence only. It is not JARVIS-VLA and does not train.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCENES_PATH = ROOT / "demo_scenes.json"
LOG_PATH = ROOT / "logs" / "gpu_action_scorer_log.md"

ACTIONS = ["attack", "use", "equip_item", "place_block", "retreat", "wait"]
FEATURES = [
    "tree_visible",
    "crafting_table_visible",
    "furnace_visible",
    "iron_ore_visible",
    "wooden_pickaxe",
    "mob_visible",
    "night",
    "has_ore_and_fuel",
]


def load_scenes() -> list[dict]:
    with SCENES_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def encode(scene: dict) -> list[float]:
    state = scene["state"]
    visible = set(state["visible_objects"])
    inventory = set(state["inventory"])
    return [
        float("tree_trunk" in visible),
        float("crafting_table" in visible),
        float("furnace" in visible),
        float("iron_ore" in visible),
        float("wooden_pickaxe" in inventory),
        float("zombie" in visible),
        float(state.get("time") == "night"),
        float({"iron_ore", "coal"} <= inventory),
    ]


def main() -> int:
    import torch

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    scenes = load_scenes()
    x = torch.tensor([encode(scene) for scene in scenes], dtype=torch.float32, device=device)

    # Deterministic toy weights. Rows are features, columns are actions.
    weights = torch.tensor(
        [
            [3.0, 0.0, 0.0, 0.0, 0.0, -0.2],
            [0.0, 2.7, 0.0, 0.0, 0.0, -0.1],
            [0.0, 3.1, 0.0, 0.0, 0.0, -0.1],
            [1.0, 0.0, -0.8, 0.0, 0.0, 0.4],
            [-0.5, 0.0, 2.4, 0.0, 0.0, 0.2],
            [-1.0, 0.0, 0.0, 0.6, 2.8, -0.3],
            [0.0, 0.0, 0.0, 1.2, 2.0, 0.1],
            [0.0, 1.2, 0.0, 0.0, 0.0, -0.1],
        ],
        dtype=torch.float32,
        device=device,
    )
    bias = torch.tensor([0.0, 0.0, -0.3, -0.2, -0.2, 0.0], dtype=torch.float32, device=device)
    scores = x @ weights + bias
    choices = scores.argmax(dim=1)

    lines = [
        "# GPU Action Scorer Log",
        "",
        "This is a toy GPU-backed action scorer. It is not JARVIS-VLA and it does not train.",
        "",
        "## Runtime",
        "",
        f"- torch: `{torch.__version__}`",
        f"- cuda_available: `{torch.cuda.is_available()}`",
        f"- device: `{torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu'}`",
        "",
        "## Results",
        "",
    ]

    for index, scene in enumerate(scenes):
        action = ACTIONS[int(choices[index].item())]
        score_dict = {
            ACTIONS[action_index]: round(float(scores[index, action_index].detach().cpu()), 3)
            for action_index in range(len(ACTIONS))
        }
        lines.extend(
            [
                f"### {scene['id']}",
                "",
                f"- selected_action: `{action}`",
                f"- scores: `{score_dict}`",
                "",
            ]
        )

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {LOG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
