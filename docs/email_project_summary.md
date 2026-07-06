# Open-World Minecraft Agent Lab

This is an unofficial student research repository for studying Minecraft open-world agents through paper reading, repository audits, bounded feasibility checks, and lightweight toy demos.

## Motivation

I am interested in Minecraft open-world agents, especially how high-level planning, memory, visual grounding, and action representation connect in embodied decision-making. Minecraft is a useful environment because simple goals often require long-horizon dependencies, visual grounding, tool constraints, inventory state, and low-level keyboard/mouse actions.

## What I Studied

I focused on four related interfaces:

- DEPS / MC-Planner: planning and dependency reasoning
- JARVIS-1: memory-augmented multimodal planning
- ROCKET-1: visual-temporal context prompting with target masks
- JARVIS-VLA: vision-language-action action prediction

The project story is:

```text
planning -> memory -> visual grounding -> action prediction
```

## What I Implemented Or Audited

- Audited official or relevant repositories for DEPS / MC-Planner, JARVIS-1, ROCKET-1, JARVIS-VLA, and MineStudio.
- Built a lightweight DEPS-style planning demo for Minecraft long-horizon tasks.
- Inspected JARVIS-1 fixed memory through aggregate statistics and built a toy memory-augmented planner.
- Built a ROCKET-1-style visual prompt demo with synthetic mask scenes.
- Built a JARVIS-VLA-style action-interface demo mapping observations and instructions to structured actions.
- Ran a tiny GPU-backed toy action scorer on the AutoDL Blackwell machine using a modern PyTorch CUDA 12.8 environment.
- Documented official reproduction blockers, including dependencies, checkpoints, datasets, simulator setup, rendering, and storage constraints.

## What I Learned

- One-shot language planning is fragile in long-horizon Minecraft tasks.
- Memory can help avoid repeated prerequisite mistakes, such as invalid tools or missing fuel.
- Language-only subgoals lose spatial detail when multiple objects or affordances are visible.
- VLA-style action prediction shifts the problem from "what should be done" to "which action should be selected next".
- Official systems require substantial setup, so lightweight preparation should be honest about what was audited, what was demonstrated, and what remains blocked.

## What I Can Contribute As An Undergraduate Intern

- Careful repository audits and reproducibility notes.
- Lightweight experiment design that isolates one research question at a time.
- Failure case analysis for Minecraft tasks.
- Small tools and demos for planning, memory retrieval, visual prompting, and action-space comparison.
- Clean documentation that distinguishes evidence from speculation.

## What I Do Not Claim

- I do not claim official end-to-end reproduction of DEPS, JARVIS-1, ROCKET-1, JARVIS-VLA, or MineStudio.
- I do not claim official Minecraft evaluation results.
- I do not claim to have trained official models or matched paper metrics.
- I do not commit model weights, checkpoints, datasets, raw videos, secrets, or external repository code.

## Key Links

- Four-interface synthesis: `docs/four_interface_comparison.md`
- Reproduction summary: `docs/reproduction_summary.md`
- Claims checklist: `docs/claims_checklist.md`
- DEPS demo: `experiments/deps-planner-demo/`
- JARVIS-1 memory demo: `experiments/jarvis1-memory-demo/`
- ROCKET-1 visual prompt demo: `experiments/rocket1-visual-prompt-demo/`
- JARVIS-VLA action demo: `experiments/jarvis-vla-action-demo/`
- Paper notes: `papers/`
