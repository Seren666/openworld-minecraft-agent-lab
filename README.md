# Open-World Minecraft Agent Lab

This is an unofficial student research repository for reading notes, repository audits, lightweight reproductions, and toy demos around open-world Minecraft agents.

Research focus:

```text
planning -> memory -> visual grounding -> action representation -> hierarchical action-space learning
```

My research interest is how these interfaces connect in embodied decision-making for Minecraft-like environments.

This repository starts from CraftJarvis planning/memory/grounding/action-interface works and is being extended toward OpenHA/CrossAgent, GRPO post-training, and world-model-based agent learning.

## For Quick Review

- [docs/quick_review.md](docs/quick_review.md): Short entry point for what this repository is, what to read first, and what is not claimed.
- [docs/action_space_taxonomy_analysis.md](docs/action_space_taxonomy_analysis.md): Exploratory OpenHA/CrossAgent metadata/config-based task taxonomy with source-scope clarification and manual sanity-check sample.
- [docs/minestudio_smoke_test.md](docs/minestudio_smoke_test.md): Bounded MineStudio install/import and simulator-readiness smoke test with current blockers.
- [docs/reproduction_summary.md](docs/reproduction_summary.md): Compact record of completed lightweight demos, audits, blockers, and evidence-supported scope.
- [docs/latest_direction_bridge.md](docs/latest_direction_bridge.md): Research bridge from planning, memory, grounding, and VLA action prediction toward OpenHA/CrossAgent, GRPO, and world models.
- [docs/four_interface_comparison.md](docs/four_interface_comparison.md): Comparison of planning, memory, visual grounding, and action representation interfaces.

## Current Focus

- Long-horizon planning
- Memory-augmented planning
- Visual-temporal grounding
- Vision-language-action representation
- Hierarchical action-space learning and GRPO-style post-training
- World-model and diffusion-model reading for future agent learning

## Progress

| Paper / System | Focus | What I did | Status | Link |
| --- | --- | --- | --- | --- |
| DEPS / MC-Planner | Planning interface | Audited the relevant repository and built a lightweight DEPS-style planning demo for Minecraft tasks. | Bounded planning pass complete | [demo](experiments/deps-planner-demo/), [note](papers/01_DEPS.md) |
| JARVIS-1 | Memory interface | Audited the official repository, inspected fixed memory through aggregate stats, and built a toy memory-augmented planner. | Audit and lightweight demo complete | [audit](experiments/jarvis1-audit/), [demo](experiments/jarvis1-memory-demo/), [note](papers/02_JARVIS-1.md) |
| ROCKET-1 | Visual grounding / mask interface | Audited the official repository and built a synthetic visual-temporal context prompting demo with mask scenes. | Audit and lightweight demo complete | [audit](experiments/rocket1-audit/), [demo](experiments/rocket1-visual-prompt-demo/), [note](papers/05_ROCKET-1.md) |
| JARVIS-VLA | Action representation / VLA interface | Audited the official repository, built a toy action-interface demo, and ran a tiny GPU action scorer. | Audit and lightweight demo complete | [audit](experiments/jarvis-vla-audit/), [demo](experiments/jarvis-vla-action-demo/), [note](papers/06_JARVIS-VLA.md) |
| OpenHA / CrossAgent | Exploratory action-space taxonomy | Analyzed metadata/config-derived task-name records, clarified source scope, added a 100-sample sanity check, and summarized failure-mode observations. | Preliminary analysis complete | [analysis](docs/action_space_taxonomy_analysis.md), [artifacts](experiments/openha-action-space-analysis/) |
| World models / diffusion | Predictive simulation for planning and RL | Added concise next-reading notes for imagined rollouts, failure prediction, data generation, and safer RL. | Conceptual note complete | [note](docs/world_model_diffusion_notes.md) |
| MineStudio minimal workflow smoke test | Minecraft agent toolchain smoke test | Package-level install/import passed; `cv2` and Java blockers resolved; simulator/rollout still blocked by `torch` and DISPLAY/Xvfb runtime stack. | Smoke test and blocker-reduction complete | [report](docs/minestudio_smoke_test.md), [artifacts](experiments/minestudio-smoke-test/) |
| GPU sanity | Infrastructure | Validated a modern PyTorch CUDA 12.8 environment on the Blackwell GPU. | Infrastructure check complete | [artifacts](experiments/gpu-sanity/) |

## What This Repository Demonstrates

- Repository audits for Minecraft open-world agent papers and codebases.
- Lightweight reproduction-style toy demos that clarify planning, memory, visual grounding, and action representation ideas.
- Bounded feasibility checks for heavier official systems.
- A conceptual bridge from action representation to hierarchical action-space learning, GRPO post-training, and world-model reading.
- A record of blockers for complete end-to-end reproduction work.

## What This Repository Does Not Claim

- It is not an official implementation from the paper authors.
- It does not claim complete reproduction of official Minecraft agent systems.
- It does not claim that official Minecraft evaluations were reproduced.
- It is not a training repository for large Minecraft agent models.
- It does not commit model weights, checkpoints, datasets, raw videos, secrets, or external repository code.

## Key Takeaways So Far

- One-shot language planning is fragile in long-horizon Minecraft tasks.
- Memory can help avoid repeated prerequisite mistakes, such as invalid tool use or missing fuel.
- Language-only subgoals lose spatial detail when multiple objects or affordances are visible.
- VLA-style action representation shifts the question from "what should be done" to "which action should be selected next".
- OpenHA/CrossAgent shift the next question to "which action abstraction should be selected now".
- World models suggest a later direction for predictive simulation, imagined rollouts, and safer RL.
- Official systems require substantial dependencies, checkpoints, datasets, and Minecraft rendering; this repo focuses on lightweight, honest preparation.

## Research Story

The current project narrative is:

```text
planning -> memory -> visual grounding -> action representation -> hierarchical action-space learning
```

The main synthesis documents are [docs/four_interface_comparison.md](docs/four_interface_comparison.md) and [docs/latest_direction_bridge.md](docs/latest_direction_bridge.md).

## Project Documents

- [docs/quick_review.md](docs/quick_review.md)
- [docs/project_overview.md](docs/project_overview.md)
- [docs/four_interface_comparison.md](docs/four_interface_comparison.md)
- [docs/latest_direction_bridge.md](docs/latest_direction_bridge.md)
- [docs/action_space_taxonomy_analysis.md](docs/action_space_taxonomy_analysis.md)
- [docs/minestudio_smoke_test.md](docs/minestudio_smoke_test.md)
- [docs/world_model_diffusion_notes.md](docs/world_model_diffusion_notes.md)
- [docs/reproduction_scope.md](docs/reproduction_scope.md)
- [docs/reproduction_summary.md](docs/reproduction_summary.md)

## Repository Layout

```text
papers/       Reading notes for core papers and systems
experiments/  Lightweight reproductions and experiment records
docs/         Research maps, summaries, setup notes, and reproduction-scope records
scripts/      Small helper scripts for setup, demos, and log collection
assets/       Figures, diagrams, and small presentation media
```
