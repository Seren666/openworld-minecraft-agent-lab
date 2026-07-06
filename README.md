# Open-World Minecraft Agent Lab

This is an unofficial student research repository for reading notes, repository audits, lightweight reproductions, and toy demos around open-world Minecraft agents.

My research interest is how high-level planning, memory, visual grounding, and action representation connect in embodied decision-making for Minecraft-like environments.

## Current Focus

- Long-horizon planning
- Memory-augmented planning
- Visual-temporal grounding
- Vision-language-action interfaces

## Progress

| Paper / System | Focus | What I did | Status | Link |
| --- | --- | --- | --- | --- |
| DEPS / MC-Planner | Planning interface | Audited the relevant repository and built a lightweight DEPS-style planning demo for Minecraft tasks. | Bounded planning pass complete | `experiments/deps-planner-demo/`, `papers/01_DEPS.md` |
| JARVIS-1 | Memory interface | Audited the official repository, inspected fixed memory through aggregate stats, and built a toy memory-augmented planner. | Audit and lightweight demo complete | `experiments/jarvis1-audit/`, `experiments/jarvis1-memory-demo/`, `papers/02_JARVIS-1.md` |
| ROCKET-1 | Visual grounding / mask interface | Audited the official repository and built a synthetic visual-temporal context prompting demo with mask scenes. | Audit and lightweight demo complete | `experiments/rocket1-audit/`, `experiments/rocket1-visual-prompt-demo/`, `papers/05_ROCKET-1.md` |
| JARVIS-VLA | Action prediction / VLA interface | Audited the official repository, built a toy action-interface demo, and ran a tiny GPU action scorer. | Audit and lightweight demo complete | `experiments/jarvis-vla-audit/`, `experiments/jarvis-vla-action-demo/`, `papers/06_JARVIS-VLA.md` |
| MineStudio | Engineering base for evaluation | Ran smoke tests and a bounded second-pass install attempt on AutoDL. | Setup still blocked | `experiments/minestudio-setup/` |
| GPU sanity | Infrastructure | Validated a modern PyTorch CUDA 12.8 environment on the Blackwell GPU. | Infrastructure check complete | `experiments/gpu-sanity/` |

## What This Repository Is

- A research preparation repository for advisor outreach.
- A reading map for Minecraft open-world agents and VLA-style systems.
- A set of bounded repository audits for official codebases.
- A collection of lightweight toy demos that clarify planning, memory, visual grounding, and action-interface ideas.
- A record of blockers for heavier official reproduction work.

## What This Repository Is Not

- It is not an official implementation from the paper authors.
- It is not a claim that official Minecraft evaluations were reproduced.
- It is not a training repository for large Minecraft agent models.
- It does not commit model weights, checkpoints, datasets, raw videos, secrets, or external repository code.

## Key Takeaways So Far

- One-shot language planning is fragile in long-horizon Minecraft tasks.
- Memory can help avoid repeated prerequisite mistakes, such as invalid tool use or missing fuel.
- Language-only subgoals lose spatial detail when multiple objects or affordances are visible.
- VLA-style action prediction shifts the question from "what should be done" to "which action should be selected next".
- Official systems require substantial dependencies, checkpoints, datasets, and Minecraft rendering; this repo focuses on lightweight, honest preparation.

## Research Story

The current project narrative is:

```text
planning -> memory -> visual grounding -> action prediction
```

The main synthesis document is `docs/four_interface_comparison.md`.

## Email Materials

- `docs/email_project_summary.md`
- `docs/four_interface_comparison.md`
- `docs/claims_checklist.md`
- `docs/reproduction_summary.md`

## Repository Layout

```text
papers/       Reading notes for core papers and systems
experiments/  Lightweight reproductions and experiment records
docs/         Research maps, summaries, setup notes, and email material
scripts/      Small helper scripts for setup, demos, and log collection
assets/       Figures, diagrams, and small presentation media
```
