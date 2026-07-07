# Reproduction Summary

This repository focuses on research preparation, not claims of official benchmark reproduction. The main story is:

```text
planning -> memory -> visual grounding -> action representation -> hierarchical action-space learning
```

This repository starts from CraftJarvis planning/memory/grounding/action-interface works and is being extended toward OpenHA/CrossAgent, GRPO post-training, and world-model-based agent learning.

## Completed Lightweight Work

| Experiment | Status | Output | Notes |
| --- | --- | --- | --- |
| DEPS / MC-Planner | Bounded planning pass complete | Repository audit, Conda notes, planning-only examples | Official demo remains blocked by API keys, controller checkpoints, simulator setup, and rendering. |
| JARVIS-1 audit | Bounded feasibility check complete | Official repo audit, dependency notes, runtime check | Official execution remains blocked by simulator, checkpoints, API access, rendering, and pinned stack issues. |
| JARVIS-1 memory demo | Lightweight local demo complete | Aggregate memory stats, toy memory retrieval, generated Markdown trace | Useful for explaining memory-augmented planning; not official JARVIS-1 inference. |
| ROCKET-1 audit | Bounded feasibility check complete | Official repo audit, dependency and SAM-2/MCP notes | Official inference requires model weights, SAM-2 checkpoints, simulator, rendering, and dependency setup. |
| ROCKET-1 visual prompt demo | Lightweight local demo complete | Synthetic grid scenes, mask prompts, SVG assets, generated Markdown trace | Demonstrates visual-temporal prompting without official checkpoints or simulator execution. |
| JARVIS-VLA audit | Bounded feasibility check complete | Official repo audit, vLLM/MineStudio rollout notes, syntax smoke | Official inference requires 7B-scale model serving, datasets, MineStudio, rendering, and careful output storage. |
| JARVIS-VLA action demo | Lightweight local demo complete | Toy action schema, rule-based selector, generated Markdown trace | Demonstrates the VLA action-representation idea without official model checkpoints. |
| JARVIS-VLA GPU action scorer | Toy GPU scorer complete | Tiny deterministic PyTorch scorer ran one forward pass on Blackwell | Infrastructure evidence only; not JARVIS-VLA inference. |
| OpenHA / CrossAgent bridge | Paper/repo audit complete | Latest-direction bridge and OpenHA/CrossAgent note | Conceptual bridge only; no weights, datasets, official rollout, SFT, or GRPO training. |
| OpenHA/CrossAgent action-space taxonomy | Exploratory metadata/config-based analysis complete | Local task-name records, category/interface summaries, failure-mode notes, and manual sanity-check sample | Rule-based and preliminary; not official model evaluation or official benchmark-size reporting. |
| World models / diffusion note | Reading direction documented | Concise world-model note | Next-step reading only; no world-model or diffusion reproduction. |
| MineStudio minimal workflow smoke test | import/module smoke test passed; simulator rollout blocked | Clean no-deps editable install, top-level import, module inventory, simulator readiness check | Simulator import is blocked by missing dependencies and display/runtime support; no rollout was run. |
| GPU sanity | Infrastructure check complete | Old torch failure documented; modern cu128 success documented | `torch 2.11.0+cu128` under `/root/autodl-tmp` supports `sm_120` and ran a small CUDA tensor workload. |

## Partially Blocked Official Systems

- MC-Planner, JARVIS-1, ROCKET-1, JARVIS-VLA, OpenHA/CrossAgent, and MineStudio all depend on substantial simulator, rendering, checkpoint, dataset, training, or model-serving infrastructure for official execution.
- Earlier pinned PyTorch stacks may not support the AutoDL Blackwell `sm_120` GPU.
- MineStudio still needs a stable dependency strategy before serious benchmark or rollout work.
- JARVIS-VLA and ROCKET-1 official inference should wait until model weights, storage, rendering, and output paths are intentionally controlled.
- OpenHA/CrossAgent official work should wait until action-space scope, model assets, datasets, and training/evaluation budget are defined.

## Evidence-Supported Scope

- I audited official or relevant repositories.
- I built lightweight demos for planning, memory, visual grounding, and action representation.
- I added a paper/repo bridge from action representation to OpenHA/CrossAgent action-space hierarchy and GRPO-style post-training.
- I added a metadata/config-based action-space taxonomy over local OpenHA/CrossAgent task-name records and representative Minecraft examples, with explicit scope limits.
- I added world-model/diffusion notes as a future reading direction.
- I ran a bounded MineStudio minimal workflow smoke test and documented the package-level success plus simulator blockers.
- I documented blockers for official end-to-end reproduction attempts.
- I kept external repos, environments, caches, large assets, and logs outside Git.
- I validated a modern Blackwell-compatible PyTorch CUDA environment for small infrastructure checks.

## Do Not Overstate

- Do not claim official end-to-end reproduction of DEPS, JARVIS-1, ROCKET-1, JARVIS-VLA, or MineStudio.
- Do not claim official OpenHA/CrossAgent execution, SFT, GRPO training, or world-model reproduction.
- Do not claim official Minecraft task success.
- Do not claim official model training or paper-metric matching.
- Do not claim toy GPU scorers are official model inference.
- Do not imply official checkpoints, datasets, raw memory files, simulator assets, or videos were committed.

## Next Recommended Experiment

Run one compact comparison across five interfaces on the same task set:

- DEPS-style dependency planning
- JARVIS-1-style memory retrieval
- ROCKET-1-style visual/mask prompting
- JARVIS-VLA-style action representation
- OpenHA/CrossAgent-style action-space selection
- metadata-based action-space pressure analysis

This is low-cost, research-relevant, and does not require simulator rendering or large assets.

## Evidence Rules

- Keep commands and environment details in Markdown.
- Commit only small notes, scripts, configs, toy JSON, summarized logs, and small figures.
- Do not commit checkpoints, datasets, raw videos, large logs, external repository code, secrets, or private machine information.
