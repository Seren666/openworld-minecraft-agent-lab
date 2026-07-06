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
| JARVIS-1 audit | Runtime audit complete; official execution blocked | Cloned JARVIS-1, recorded upstream commit, inspected requirements, ran safe import/help checks, and tested the official-style PyTorch stack. | `experiments/jarvis1-audit/feasibility_report.md`, `experiments/jarvis1-audit/runtime_check.md`, `papers/02_JARVIS-1.md` | Use memory analysis as the near-term artifact; defer simulator evaluation until CUDA, MCP, rendering, and checkpoints are stable. |
| JARVIS-1 memory demo | Lightweight demo complete | Analyzed official fixed memory through aggregate stats and built an original toy memory-augmented planning demo. | `experiments/jarvis1-memory-demo/memory_analysis.md`, `experiments/jarvis1-memory-demo/logs/example_run.md` | Compare memory retrieval with DEPS-style dependency planning on a few shared tasks. |
| MineStudio setup | Second-pass install still blocked | Cloned MineStudio, created `minestudio-test`, verified no-deps source import, and ran a bounded second-pass dependency check. | `experiments/minestudio-setup/install_notes.md`, `experiments/minestudio-setup/second_pass_install.md`, `experiments/minestudio-setup/run_logs.md` | Free disk space, install dependencies in smaller groups, then test PyTorch, OpenCV, `MinecraftSim`, and rendering. |
| GPU sanity check | Infrastructure blocked by PyTorch/CUDA compatibility | Confirmed Blackwell GPUs are visible, but official pinned PyTorch cannot execute CUDA kernels; newer CUDA 12.8 install failed due root filesystem space. | `experiments/gpu-sanity/gpu_check_log.md`, `experiments/jarvis1-audit/runtime_check.md` | Install a Blackwell-compatible PyTorch build after freeing or expanding root filesystem space. |
| Minecraft task dependency analysis | In progress | Organize tasks, dependencies, failure cases, and gameplay notes. | `experiments/minecraft-task-analysis/` | Expand dependency graph examples. |
| Mini VLA gridworld | Planned | Create a lightweight VLA-style sandbox before Minecraft-scale experiments. | `experiments/mini-vla-gridworld/` | Define minimal action and observation space. |
| Benchmark evaluation | Planned | Compare tasks, metrics, and failure modes across systems. | `docs/reproduction_summary.md` | Add evaluation criteria after MineStudio setup. |

## Current Focus

- DEPS planner demo
- JARVIS-1 memory-augmented planning demo
- MineStudio setup blockers
- Minecraft task dependency analysis

## Future Work

- Benchmark evaluation
- Failure case analysis
- Action space comparison
- Lightweight VLA demo
- Blackwell-compatible PyTorch environment setup

## Repository Layout

```text
papers/       Reading notes for core papers and systems
experiments/  Lightweight reproductions and experiment records
docs/         Research maps, summaries, setup notes, and presentation material
scripts/      Small helper scripts for setup, demos, and log collection
assets/       Figures, diagrams, and small presentation media
```
