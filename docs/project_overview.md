# Project Overview

Open-World Minecraft Agent Lab is an unofficial student research repository for studying Minecraft open-world agents through paper reading, repository audits, bounded feasibility checks, and lightweight toy demos.

## Motivation

Minecraft is a useful embodied-AI environment because simple goals often require long-horizon dependencies, visual grounding, tool constraints, inventory state, and low-level keyboard/mouse actions. This project studies how high-level planning, memory, visual grounding, action representation, and hierarchical action-space selection connect in that setting.

This repository starts from CraftJarvis planning/memory/grounding/action-interface works and is being extended toward OpenHA/CrossAgent, GRPO post-training, and world-model-based agent learning.

## Research Thread

```text
planning -> memory -> visual grounding -> action representation -> hierarchical action-space learning
```

| Component | Research role |
| --- | --- |
| DEPS / MC-Planner | Dependency-aware planning for long-horizon tasks. |
| JARVIS-1 | Memory-augmented multimodal planning. |
| ROCKET-1 | Visual-temporal grounding through target/mask context. |
| JARVIS-VLA | Vision-language-action representation from observation to action. |
| OpenHA / CrossAgent | Hierarchical action-space learning and dynamic cross-level action selection. |
| World models / diffusion models | Future direction for predictive simulation and imagined rollouts. |

## Completed Research Preparation

- Audited official or relevant repositories for DEPS / MC-Planner, JARVIS-1, ROCKET-1, JARVIS-VLA, OpenHA/CrossAgent, and MineStudio.
- Built a lightweight DEPS-style planning demo for Minecraft long-horizon tasks.
- Inspected JARVIS-1 fixed memory through aggregate statistics and built a toy memory-augmented planner.
- Built a ROCKET-1-style visual prompt demo with synthetic mask scenes.
- Built a JARVIS-VLA-style action-representation demo mapping observations and instructions to structured actions.
- Ran a tiny GPU-backed toy action scorer on the AutoDL Blackwell machine using a modern PyTorch CUDA 12.8 environment.
- Added an OpenHA/CrossAgent bridge for action-space hierarchy, SFT, and GRPO-style post-training.
- Added concise world-model and diffusion-model notes as future research directions.
- Documented official reproduction blockers, including dependencies, checkpoints, datasets, simulator setup, rendering, and storage constraints.

## Key Findings So Far

- One-shot language planning is fragile in long-horizon Minecraft tasks.
- Memory can help avoid repeated prerequisite mistakes, such as invalid tools or missing fuel.
- Language-only subgoals lose spatial detail when multiple objects or affordances are visible.
- VLA-style action representation shifts the problem from "what should be done" to "which action should be selected next".
- OpenHA/CrossAgent shift the next problem to hierarchical action-space learning.
- World models suggest a future route for imagined rollouts, failure prediction, and safer RL, but this is only a reading direction here.
- Official systems require substantial setup, so this repository separates what was audited, what was demonstrated with toy examples, and what remains blocked.

## Reproduction Scope

- This repository does not claim full reproduction or official end-to-end reproduction of DEPS, JARVIS-1, ROCKET-1, JARVIS-VLA, OpenHA/CrossAgent, or MineStudio.
- It does not claim official Minecraft evaluation results.
- It does not claim official model training, GRPO post-training, world-model reproduction, or paper-metric matching.
- It does not commit model weights, checkpoints, datasets, raw videos, secrets, or external repository code.

## Key Links

- Four-interface synthesis: `docs/four_interface_comparison.md`
- Latest-direction bridge: `docs/latest_direction_bridge.md`
- World-model notes: `docs/world_model_diffusion_notes.md`
- Reproduction summary: `docs/reproduction_summary.md`
- Reproduction scope: `docs/reproduction_scope.md`
- DEPS demo: `experiments/deps-planner-demo/`
- JARVIS-1 memory demo: `experiments/jarvis1-memory-demo/`
- ROCKET-1 visual prompt demo: `experiments/rocket1-visual-prompt-demo/`
- JARVIS-VLA action demo: `experiments/jarvis-vla-action-demo/`
- Paper notes: `papers/`
