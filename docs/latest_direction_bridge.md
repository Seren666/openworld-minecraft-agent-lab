# Latest Direction Bridge: OpenHA, CrossAgent, GRPO, And World Models

This note extends the repository story beyond earlier CraftJarvis planning, memory, grounding, and VLA-interface papers.

```text
planning -> memory -> visual grounding -> action representation -> hierarchical action-space learning
```

This repository starts from CraftJarvis planning/memory/grounding/action-interface works and is being extended toward OpenHA/CrossAgent, GRPO post-training, and world-model-based agent learning.

## Audit Snapshot

| Item | Finding |
| --- | --- |
| Repository | https://github.com/CraftJarvis/OpenHA |
| Branch audited | `main` |
| Commit audited | `606efc69e945bd02c700e584136bcc105d22f122` |
| CrossAgent folder | Present at `CrossAgent/`, with `MTRL/`, `SFT/`, and `STRL/` subfolders |
| README focus | Open-source hierarchical agentic models for Minecraft using high-level planning, control, and Chain of Action |
| OpenHA paper | https://arxiv.org/abs/2509.13347 |
| CrossAgent paper | https://arxiv.org/abs/2512.09706 |
| Install stack from repo | Python 3.10, OpenJDK 8, MineStudio, PyTorch CUDA wheel guidance, vLLM, SAM-2 related setup |
| Public assets | README links Hugging Face model repositories and datasets for OpenHA and CrossAgent; none were downloaded for this repository |
| Reproduction status here | Paper/repo audit and conceptual bridge only; no weights, datasets, or simulator rollout downloaded |

## Public Assets Listed By The README

The official README lists public Hugging Face assets. This audit records availability only; it does not download or use them.

| Category | Assets listed |
| --- | --- |
| OpenHA models | `OpenHA-7B`, `OpenHA-Qwen2.5-VL-7B`, `OpenHA-VPT`, `SAM2-OpenHA` |
| OpenHA datasets | `OpenHA-CoA-2B`, `OpenHA-Task-2B`, `OpenHA-VPT-2B` |
| CrossAgent models | `OpenHA-CrossAgent-SFT-7B`, `OpenHA-CrossAgent-7B` |
| CrossAgent datasets | `OpenHA-CrossAgent-CoA-0.2B`, `OpenHA-CrossAgent-SFT-0.2B`, `OpenHA-CrossAgent-GRPO-0.02B` |

The README also includes a multi-GPU vLLM serving example. I did not run that command because this task is a bounded audit and the project default is single-GPU lightweight testing unless a task explicitly requires more.

## Why The Earlier Papers Are Not The Endpoint

The earlier notes in this repository isolate four important interfaces:

- DEPS / MC-Planner asks how to decompose long-horizon Minecraft goals into dependency-aware plans.
- JARVIS-1 asks how memory can reduce repeated planning mistakes.
- ROCKET-1 asks how visual/mask context can ground ambiguous language goals.
- JARVIS-VLA asks how a model can represent visual-language context as executable actions.

Together, these still leave a central open question: what action space should the agent use at each moment? A Minecraft agent may need high-level skills, mid-level structured actions, or low-level keyboard/mouse control depending on the task phase. A single fixed action interface can be too coarse for precise control or too low-level for long-horizon planning.

## OpenHA: Action-Space Comparison And Chain Of Action

OpenHA pushes the story toward action-space hierarchy. The main research question becomes:

```text
Which level of action abstraction is appropriate for the current task and state?
```

OpenHA is relevant because it treats action representation as a first-class research problem rather than a hidden controller detail. Its README positions the project around hierarchical agentic models and highlights a Chain of Action view, where the agent reasons across levels of abstraction.

For this repository, OpenHA is a bridge from "represent the next executable action" to "choose the right action space for the next decision." That is exactly the gap left after JARVIS-VLA-style action representation.

## CrossAgent: Dynamic Cross-Level Action Selection

The CrossAgent folder in the OpenHA repository makes the next direction more explicit. It contains subfolders for:

- `MTRL`: multi-task reinforcement learning style material
- `SFT`: supervised fine-tuning material
- `STRL`: self-training or staged RL-related material

The CrossAgent paper is framed around a unified agent that can dynamically select heterogeneous action spaces. In practical terms, this means the model is not limited to one action granularity. It can learn when to use higher-level skills and when to switch to lower-level actions.

This is a natural continuation of the existing repository story:

```text
planning tells us what should happen
memory reminds us what usually goes wrong
visual grounding identifies what the agent should interact with
VLA action representation selects an executable next step
CrossAgent asks which action level should be used for that step
```

## Why GRPO Matters

CrossAgent's direction points toward post-training rather than only imitation. SFT can teach the model the format and distribution of good actions, but long-horizon Minecraft behavior also needs feedback from success, failure, and task progress.

GRPO-style post-training is relevant because it can optimize action choices using grouped rollout feedback without requiring a separate value model in the same way as some older RLHF-style pipelines. For Minecraft agents, the important conceptual point is not that this repository has run GRPO. It has not. The point is that GRPO gives a language/VLA policy a way to improve hierarchical action-space decisions from task-level outcomes.

Safe claim for this repository:

```text
I audited the OpenHA/CrossAgent direction and identified GRPO-based post-training as a next reading target for hierarchical action-space learning.
```

Unsafe claim:

```text
I trained CrossAgent with GRPO.
```

## World Models And Diffusion Models

World models add another layer: instead of only choosing actions in the live environment, an agent can learn or query a predictive model of future observations. Diffusion and video diffusion models are relevant because they can model temporally coherent visual futures.

For Minecraft agents, this could support:

- imagined rollouts before executing a risky plan
- failure prediction before wasting environment steps
- synthetic data generation for rare situations
- safer RL by testing plans in a learned simulator
- planning over predicted visual consequences instead of only text descriptions

This repository does not reproduce a world model. The correct positioning is that world/diffusion models are a next-step reading direction that may connect Minecraft planning, VLA control, and RL training.

## Lightweight Reproduction Feasibility

| Component | Feasibility | Reason |
| --- | --- | --- |
| OpenHA official rollout | Not lightweight | Requires MineStudio/Minecraft environment, model serving, rendering, and checkpoint/dataset decisions. |
| OpenHA repository audit | Lightweight | README, package metadata, folder layout, and paper links can be inspected safely. |
| CrossAgent official training | Not lightweight | SFT/GRPO/RL-style training needs datasets, compute, model checkpoints, and careful experiment management. |
| CrossAgent conceptual toy demo | Lightweight | A small script could compare high-level, mid-level, and low-level action choices on toy task states. |
| World-model reproduction | Not lightweight | Requires video/model training or large pretrained assets. |
| World-model reading note | Lightweight | Useful for research positioning without claiming unsupported results. |

## Added Repository Analysis

The repository now includes a lightweight OpenHA/CrossAgent action-space taxonomy:

- `docs/action_space_taxonomy_analysis.md`
- `experiments/openha-action-space-analysis/`

The analysis uses public local metadata/config-derived task-name records plus bounded representative additions. It should not be read as the official OpenHA/CrossAgent benchmark size; the paper framing describes an over-800-task benchmark. The detailed exploratory statistics classify local records by category, interface pressure, required information type, and likely fixed-action-space failure, while the main takeaway is qualitative: dynamic action-space switching appears relevant for a meaningful subset of records rather than every task.

## Next Study Targets

1. Read OpenHA for action-space hierarchy and Chain of Action.
2. Read CrossAgent for dynamic cross-level action selection, SFT, and GRPO post-training.
3. Compare OpenHA/CrossAgent with the existing JARVIS-VLA action-interface demo.
4. Read one or two world-model or video-diffusion-for-agents papers to understand predictive simulation.
5. Refine the core research question: how should Minecraft agents choose between high-level skills, mid-level symbolic actions, and low-level controls?

## Safe Summary

This is a paper/repo audit and conceptual bridge. It does not run official OpenHA, train CrossAgent, download large datasets, use model weights, or claim official Minecraft evaluation results.
