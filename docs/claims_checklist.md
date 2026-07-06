# Claims Checklist

Use this checklist before writing emails, README text, slides, or summaries.

## Safe To Say

- I audited official or relevant repositories for Minecraft agent papers.
- I built lightweight demos to clarify paper ideas.
- I studied DEPS, JARVIS-1, ROCKET-1, and JARVIS-VLA.
- I documented blockers for official reproduction attempts.
- I explored planning, memory, visual grounding, and action-interface questions.
- I ran bounded feasibility checks on an AutoDL machine.
- I validated that a modern PyTorch CUDA 12.8 environment can run a tiny tensor workload on the Blackwell GPU.
- I kept large assets, external repos, caches, and temporary files outside the GitHub repository.

## Not Safe To Say

- I fully reproduced DEPS.
- I fully reproduced JARVIS-1.
- I fully reproduced ROCKET-1.
- I fully reproduced JARVIS-VLA.
- I fully reproduced MineStudio.
- I trained the official models.
- I ran the official Minecraft evaluation.
- I matched paper results.
- I downloaded or used official model weights unless a future log clearly documents that.
- I solved the full Minecraft simulator and rendering stack.

## Prefer This Wording

| Avoid | Use instead |
| --- | --- |
| reproduced the paper | built a lightweight reproduction-style demo |
| ran the official system | audited the official repository and documented blockers |
| proved the method works | illustrated the core interface idea with a toy demo |
| GPU experiment validates the model | GPU check demonstrates infrastructure readiness |
| completed MineStudio setup | ran bounded MineStudio smoke tests and documented unresolved blockers |

## Email Guardrail

The strongest honest statement is:

```text
I prepared a research-oriented repository with reading notes, repository audits, bounded feasibility checks, and lightweight toy demos that connect planning, memory, visual grounding, and action prediction for Minecraft open-world agents.
```
