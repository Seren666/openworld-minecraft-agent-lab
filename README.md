# Open-World Minecraft Agent Lab

This is an unofficial student research repository for reading notes, lightweight reproductions, and experiment logs around open-world Minecraft agents.

## Motivation

Minecraft is a useful testbed for open-ended embodied AI: long-horizon planning, sparse rewards, visual-language-action policies, skill reuse, and agentic tool use all appear in a concrete environment. This repository organizes reading and small-scale reproductions for Minecraft open-world agents, VLA models, hierarchical planning, and embodied AI systems.

## Paper Roadmap

| Order | Paper / System | Focus |
| --- | --- | --- |
| 1 | DEPS | Planning with dependency-aware task decomposition |
| 2 | JARVIS-1 | Open-world multimodal agent behavior in Minecraft |
| 3 | GROOT | Scalable policy and skill learning for open-ended tasks |
| 4 | OmniJARVIS | Generalist Minecraft agent capabilities |
| 5 | ROCKET-1 | Data, policy, and evaluation for open-world agents |
| 6 | JARVIS-VLA | Vision-language-action modeling for Minecraft control |
| 7 | OpenHA | Hierarchical agent design and open-world evaluation |

## Reproduction Progress

| Paper / Project | Status | What I did | Evidence | Next step |
| --- | --- | --- | --- | --- |
| DEPS / MC-Planner | Bounded planning pass complete | Inspected MC-Planner, created `mc-planner-test`, documented official blockers, and wrote a lightweight DEPS-style planning demo. | `experiments/deps-planner-demo/logs/run_log.md`, `experiments/deps-planner-demo/task_examples.md`, `papers/01_DEPS.md` | Prepare keys, MC-Simulator, MineCLIP, controller checkpoint, and one short official simulator run if needed. |
| MineStudio setup | Smoke test blocked by dependency install timeout | Cloned MineStudio, created `minestudio-test`, verified Python/OpenJDK, and confirmed no-deps package import; full dependency install timed out. | `experiments/minestudio-setup/install_notes.md`, `experiments/minestudio-setup/run_logs.md` | Stabilize dependency install, then test PyTorch, OpenCV, `MinecraftSim`, and rendering. |
| Minecraft task dependency analysis | In progress | Organize tasks, dependencies, failure cases, and gameplay notes. | `experiments/minecraft-task-analysis/` | Expand dependency graph examples. |
| Mini VLA gridworld | Planned | Create a lightweight VLA-style sandbox before Minecraft-scale experiments. | `experiments/mini-vla-gridworld/` | Define minimal action and observation space. |
| Benchmark evaluation | Planned | Compare tasks, metrics, and failure modes across systems. | `docs/reproduction_summary.md` | Add evaluation criteria after MineStudio setup. |

## Current Focus

- DEPS planner demo
- MineStudio setup
- Minecraft task dependency analysis

## Future Work

- Benchmark evaluation
- Failure case analysis
- Action space comparison
- Lightweight VLA demo

## Repository Layout

```text
papers/       Reading notes for core papers and systems
experiments/  Lightweight reproductions and experiment records
docs/         Research maps, summaries, setup notes, and presentation material
scripts/      Small helper scripts for setup, demos, and log collection
assets/       Figures, diagrams, and small presentation media
```
