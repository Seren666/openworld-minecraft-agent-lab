# Reproduction Scope

Use this document to keep repository wording aligned with the actual evidence in the paper notes, repository audits, lightweight demos, and summarized logs.

## What This Repository Demonstrates

- Official or relevant repository audits for Minecraft agent papers.
- Lightweight reproduction-style toy demos that clarify paper ideas without claiming official reproduction.
- Reading notes for DEPS, JARVIS-1, ROCKET-1, JARVIS-VLA, OpenHA/CrossAgent, and world-model directions.
- Documentation of blockers for official reproduction attempts.
- Planning, memory, visual grounding, action representation, and hierarchical action-space learning analysis.
- Bounded feasibility checks on an AutoDL machine.
- Infrastructure notes for a modern PyTorch CUDA 12.8 environment on the Blackwell GPU.
- Repository hygiene that keeps large assets, external repos, caches, temporary files, secrets, and private machine details outside Git.

## What This Repository Does Not Claim

- Full reproduction or official end-to-end reproduction of DEPS, JARVIS-1, ROCKET-1, JARVIS-VLA, MineStudio, or OpenHA.
- CrossAgent training.
- GRPO post-training.
- World-model or diffusion-model reproduction.
- Official model training.
- Official Minecraft evaluation runs.
- Paper-metric matching.
- Undocumented model-weight or dataset usage.
- Solving the full Minecraft simulator and rendering stack.

## Preferred Wording

| Avoid | Use instead |
| --- | --- |
| reproduced the paper | built a lightweight reproduction-style demo |
| ran the official system | audited the official repository and documented blockers |
| proved the method works | illustrated the core interface idea with a toy demo |
| GPU experiment validates the model | GPU check demonstrates infrastructure readiness |
| completed MineStudio setup | ran bounded MineStudio smoke tests and documented unresolved blockers |
| trained CrossAgent | audited OpenHA/CrossAgent and identified SFT + GRPO as next reading targets |
| reproduced a world model | added a concise world-model reading note |

## Research-Scope Summary

The strongest honest project statement is:

```text
I prepared a research-oriented repository with reading notes, repository audits, bounded feasibility checks, and lightweight toy demos that connect planning, memory, visual grounding, action representation, hierarchical action-space learning, and future world-model directions for Minecraft open-world agents.
```
