# ROCKET-1 Visual Prompt Demo

This folder contains a lightweight visual-temporal context prompting demo inspired by ROCKET-1. It is not an official reproduction and does not use ROCKET-1 checkpoints, SAM-2 checkpoints, Minecraft screenshots, or a simulator.

## Purpose

ROCKET-1 argues that language-only subgoal instructions can lose spatial detail. In Minecraft, "mine the tree" or "use the station" may not identify which object to interact with, where it is, or whether the interaction is approach, mine, use, craft, switch, or hunt.

This toy demo shows how a visual mask plus interaction type can reduce ambiguity.

## Scenarios

- Mine the correct tree among multiple objects.
- Approach/use the furnace instead of the crafting table.
- Switch target from stone to iron ore.
- Avoid mining the wrong block.
- Use a shelter door instead of breaking a wall.

## Run

From the repository root:

```bash
python experiments/rocket1-visual-prompt-demo/visual_prompt_demo.py
```

The script writes:

```text
experiments/rocket1-visual-prompt-demo/logs/example_run.md
experiments/rocket1-visual-prompt-demo/assets/*.svg
```

## What Counts As Evidence

The evidence is conceptual: each scenario has a language-only instruction, a failure mode, a mask/visual prompt representation, an interaction type, and a short explanation of why visual-temporal context helps.

It does not measure policy success and should not be described as official ROCKET-1 inference.
