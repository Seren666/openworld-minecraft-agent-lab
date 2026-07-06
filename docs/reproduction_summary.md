# Reproduction Summary

This repository focuses on research preparation, not claims of official benchmark reproduction. The main story is:

```text
planning -> memory -> visual grounding -> action prediction
```

## Completed Lightweight Work

| Experiment | Status | Output | Notes |
| --- | --- | --- | --- |
| DEPS / MC-Planner | Bounded planning pass complete | Repository audit, Conda notes, planning-only examples | Official demo remains blocked by API keys, controller checkpoints, simulator setup, and rendering. |
| JARVIS-1 audit | Bounded feasibility check complete | Official repo audit, dependency notes, runtime check | Official execution remains blocked by simulator, checkpoints, API access, rendering, and pinned stack issues. |
| JARVIS-1 memory demo | Lightweight local demo complete | Aggregate memory stats, toy memory retrieval, generated Markdown trace | Useful for explaining memory-augmented planning; not official JARVIS-1 inference. |
| ROCKET-1 audit | Bounded feasibility check complete | Official repo audit, dependency and SAM-2/MCP notes | Official inference requires model weights, SAM-2 checkpoints, simulator, rendering, and dependency setup. |
| ROCKET-1 visual prompt demo | Lightweight local demo complete | Synthetic grid scenes, mask prompts, SVG assets, generated Markdown trace | Demonstrates visual-temporal prompting without official checkpoints or simulator execution. |
| JARVIS-VLA audit | Bounded feasibility check complete | Official repo audit, vLLM/MineStudio rollout notes, syntax smoke | Official inference requires 7B-scale model serving, datasets, MineStudio, rendering, and careful output storage. |
| JARVIS-VLA action demo | Lightweight local demo complete | Toy action schema, rule-based selector, generated Markdown trace | Demonstrates the VLA action-interface idea without official model checkpoints. |
| JARVIS-VLA GPU action scorer | Toy GPU scorer complete | Tiny deterministic PyTorch scorer ran one forward pass on Blackwell | Infrastructure evidence only; not JARVIS-VLA inference. |
| MineStudio setup | Bounded setup checks blocked | Smoke tests, second-pass install notes | Full dependency setup remains unresolved; simulator imports need more controlled setup. |
| GPU sanity | Infrastructure check complete | Old torch failure documented; modern cu128 success documented | `torch 2.11.0+cu128` under `/root/autodl-tmp` supports `sm_120` and ran a small CUDA tensor workload. |

## Partially Blocked Official Systems

- MC-Planner, JARVIS-1, ROCKET-1, JARVIS-VLA, and MineStudio all depend on substantial simulator, rendering, checkpoint, dataset, or model-serving infrastructure.
- Earlier pinned PyTorch stacks may not support the AutoDL Blackwell `sm_120` GPU.
- MineStudio still needs a stable dependency strategy before serious benchmark or rollout work.
- JARVIS-VLA and ROCKET-1 official inference should wait until model weights, storage, rendering, and output paths are intentionally controlled.

## Safe To Mention In Email

- I audited official or relevant repositories.
- I built lightweight demos for planning, memory, visual grounding, and action prediction.
- I documented blockers for official end-to-end reproduction attempts.
- I kept external repos, environments, caches, large assets, and logs outside Git.
- I validated a modern Blackwell-compatible PyTorch CUDA environment for small infrastructure checks.

## Do Not Overstate

- Do not claim official end-to-end reproduction of DEPS, JARVIS-1, ROCKET-1, JARVIS-VLA, or MineStudio.
- Do not claim official Minecraft task success.
- Do not claim official model training or paper-metric matching.
- Do not claim toy GPU scorers are official model inference.
- Do not imply official checkpoints, datasets, raw memory files, simulator assets, or videos were committed.

## Next Recommended Experiment

Run one compact comparison across four interfaces on the same task set:

- DEPS-style dependency planning
- JARVIS-1-style memory retrieval
- ROCKET-1-style visual/mask prompting
- JARVIS-VLA-style action prediction

This is low-cost, email-relevant, and does not require simulator rendering or large assets.

## Evidence Rules

- Keep commands and environment details in Markdown.
- Commit only small notes, scripts, configs, toy JSON, summarized logs, and small figures.
- Do not commit checkpoints, datasets, raw videos, large logs, external repository code, secrets, or private machine information.
