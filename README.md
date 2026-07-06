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
| 5 | ROCKET-1 | Visual-temporal context prompting for grounded interaction |
| 6 | JARVIS-VLA | Vision-language-action modeling for Minecraft control |
| 7 | OpenHA | Hierarchical agent design and open-world evaluation |

## Reproduction Progress

| Paper / Project | Status | What I did | Evidence | Next step |
| --- | --- | --- | --- | --- |
| DEPS / MC-Planner | Bounded planning pass complete | Inspected MC-Planner, created `mc-planner-test`, documented official blockers, and wrote a lightweight DEPS-style planning demo. | `experiments/deps-planner-demo/logs/run_log.md`, `experiments/deps-planner-demo/task_examples.md`, `papers/01_DEPS.md` | Prepare keys, MC-Simulator, MineCLIP, controller checkpoint, and one short official simulator run if needed. |
| JARVIS-1 audit | Runtime audit complete; official execution blocked | Cloned JARVIS-1, recorded upstream commit, inspected requirements, ran safe import/help checks, and tested the official-style PyTorch stack. | `experiments/jarvis1-audit/feasibility_report.md`, `experiments/jarvis1-audit/runtime_check.md`, `papers/02_JARVIS-1.md` | Use memory analysis as the near-term artifact; defer simulator evaluation until CUDA, MCP, rendering, and checkpoints are stable. |
| JARVIS-1 memory demo | Lightweight demo complete | Analyzed official fixed memory through aggregate stats and built an original toy memory-augmented planning demo. | `experiments/jarvis1-memory-demo/memory_analysis.md`, `experiments/jarvis1-memory-demo/logs/example_run.md` | Compare memory retrieval with DEPS-style dependency planning on a few shared tasks. |
| MineStudio setup | Second-pass install still blocked | Cloned MineStudio, created `minestudio-test`, verified no-deps source import, and ran a bounded second-pass dependency check. | `experiments/minestudio-setup/install_notes.md`, `experiments/minestudio-setup/second_pass_install.md`, `experiments/minestudio-setup/run_logs.md` | Free disk space, install dependencies in smaller groups, then test PyTorch, OpenCV, `MinecraftSim`, and rendering. |
| ROCKET-1 audit | Bounded repository audit complete | Cloned ROCKET-1, recorded upstream commit, inspected README, dependencies, SAM-2/MCP requirements, and feasible demo paths. | `experiments/rocket1-audit/feasibility_report.md`, `papers/05_ROCKET-1.md` | Defer official inference until SAM-2 checkpoints, model weights, simulator, and rendering are intentionally prepared. |
| ROCKET-1 visual prompt demo | Lightweight demo complete | Built a synthetic grid demo comparing language-only instructions with mask/interaction prompts. | `experiments/rocket1-visual-prompt-demo/logs/example_run.md`, `experiments/rocket1-visual-prompt-demo/assets/` | Compare mask prompting with DEPS/JARVIS memory planning on shared Minecraft subgoals. |
| JARVIS-VLA audit | Bounded repository audit complete | Cloned JARVIS-VLA to the AutoDL data disk, recorded upstream commit, inspected README, requirements, vLLM inference, dataset/model links, and evaluation scripts. | `experiments/jarvis-vla-audit/feasibility_report.md`, `papers/06_JARVIS-VLA.md` | Defer official inference until model weights, vLLM, MineStudio, rendering, and storage are deliberately prepared. |
| JARVIS-VLA action demo | Lightweight demo complete | Built a toy action-interface demo mapping observation, instruction, and state to structured game actions. | `experiments/jarvis-vla-action-demo/logs/example_run.md` | Compare action-interface decisions against DEPS planning, JARVIS memory, and ROCKET visual prompts. |
| JARVIS-VLA GPU action scorer | Toy GPU scorer complete | Ran a tiny deterministic PyTorch scorer on Blackwell using the data-disk CUDA 12.8 environment. | `experiments/jarvis-vla-action-demo/logs/gpu_action_scorer_log.md` | Use only as infrastructure evidence; do not claim official JARVIS-VLA inference. |
| GPU sanity check | Modern PyTorch CUDA works; official pinned stacks still need care | Confirmed Blackwell GPUs are visible; old JARVIS pinned torch fails, but `torch 2.11.0+cu128` under `/root/autodl-tmp` executes a CUDA tensor workload. | `experiments/gpu-sanity/gpu_check_log.md`, `experiments/gpu-sanity/blackwell_torch_cu128.md` | Use a Blackwell-compatible PyTorch stack for future ROCKET-1/MineStudio attempts where compatible. |
| Minecraft task dependency analysis | In progress | Organize tasks, dependencies, failure cases, and gameplay notes. | `experiments/minecraft-task-analysis/` | Expand dependency graph examples. |
| Mini VLA gridworld | Planned | Create a lightweight VLA-style sandbox before Minecraft-scale experiments. | `experiments/mini-vla-gridworld/` | Define minimal action and observation space. |
| Benchmark evaluation | Planned | Compare tasks, metrics, and failure modes across systems. | `docs/reproduction_summary.md` | Add evaluation criteria after MineStudio setup. |

## Current Focus

- DEPS planner demo
- JARVIS-1 memory-augmented planning demo
- ROCKET-1 visual prompt demo
- JARVIS-VLA action-interface demo
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
