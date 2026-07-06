# Roadmap

## Phase 1: Reading Map

- Read and summarize DEPS, JARVIS-1, GROOT, OmniJARVIS, ROCKET-1, JARVIS-VLA, and OpenHA.
- Extract task representations, action spaces, planning mechanisms, datasets, and evaluation protocols.
- Build a comparison table for assumptions, reproducibility, and compute requirements.

## Phase 2: Lightweight Reproduction

- Implement a DEPS-style planner demo with prompt examples and small task graphs.
- Add a JARVIS-1-style memory-augmented planning demo using toy memory and aggregate-only official memory analysis.
- Add a ROCKET-1-style visual prompt demo using synthetic masks, interaction types, and temporal context.
- Set up MineStudio and document installation issues on local and AutoDL environments.
- Build a Minecraft task taxonomy and dependency graph for common survival tasks.

## Phase 3: Experiment Tracking

- Keep small Markdown run logs under `experiments/`.
- Store small screenshots that explain setup or qualitative behavior.
- Keep large datasets, checkpoints, videos, and generated outputs outside Git.
- Track infrastructure blockers separately from research results, especially CUDA/PyTorch compatibility and simulator setup.

## Phase 4: Mini VLA Sandbox

- Create a compact gridworld environment for vision-language-action experiments.
- Compare action abstraction choices before moving to heavier Minecraft experiments.
- Record failure cases and evaluation notes.

## Phase 5: Presentation

- Prepare diagrams, paper summaries, and reproduction findings for GitHub.
- Convert research notes into a clear project narrative.
- Draft email and outreach materials for advisors or collaborators.
- Emphasize lightweight evidence honestly: planning traces, memory analysis, environment audit, and known blockers.

## Immediate Next Steps

- Compare DEPS-style dependency planning with JARVIS-1-style memory retrieval on shared Minecraft tasks.
- Use the working Blackwell-compatible PyTorch CUDA 12.8 environment as the starting point for future GPU-backed Minecraft agent code.
- Extend the ROCKET-1 visual prompt demo into a small comparison with DEPS/JARVIS-style subgoal planning.
- Defer full MineStudio and JARVIS-1 simulator runs until dependency, Java, rendering, and checkpoint requirements are controlled.
