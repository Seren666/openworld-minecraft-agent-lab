# Roadmap

This roadmap is intentionally practical and research-oriented. The goal is to keep the repository focused on preparation, judgment, and clear research direction before attempting expensive official training or evaluation.

## Current Story

The repository now compares four interfaces for Minecraft open-world agents and extends them toward the latest action-space direction:

```text
DEPS planning -> JARVIS-1 memory -> ROCKET-1 visual grounding -> JARVIS-VLA action prediction -> OpenHA/CrossAgent dynamic action-space selection
```

This repository starts from CraftJarvis planning/memory/grounding/action-interface works and is being extended toward OpenHA/CrossAgent, GRPO post-training, and world-model-based agent learning.

The immediate aim is to make this story clear enough for a researcher to understand the project scope quickly.

## Near-Term Research Preparation

1. Polish paper notes and make terminology consistent across `papers/`.
2. Add a GROOT reading note focused on video instruction, goal representation, and open-ended behavior.
3. Add an OmniJARVIS reading note focused on unified VLA tokenization and generalist Minecraft control.
4. Refine the OpenHA/CrossAgent bridge into a compact action-space comparison diagram.
5. Add a short reading comparison between world models, video diffusion, and model-based RL for open-world agents.

## Focused Future Research Directions

Choose one focused direction instead of starting large training immediately:

| Direction | Possible student-scale work |
| --- | --- |
| Benchmark evaluation | Define a small task set and compare failure modes across interfaces. |
| Memory retrieval analysis | Study when retrieved memory helps or hurts long-horizon planning. |
| Failure case analysis | Build a taxonomy for tool, recipe, spatial, and action-selection failures. |
| Visual prompt interface | Extend the ROCKET-1 toy demo into more structured mask/affordance examples. |
| Action space comparison | Compare discrete action schemas for Minecraft-style VLA control. |
| GRPO post-training reading | Study when outcome-based post-training helps dynamic action-level selection. |
| World-model planning | Compare imagined-rollout ideas without downloading large model weights or datasets. |

## Deferred Until There Is A Clear Research Direction

- Full official model training.
- Large checkpoint or dataset downloads.
- Long Minecraft rollout jobs.
- Multi-GPU experiments.
- Large video generation.
- Official CrossAgent SFT/GRPO training.
- World-model or diffusion-model training.

## Engineering Rules

- Keep external repositories, environments, caches, logs, checkpoints, datasets, and temporary files under `/root/autodl-tmp` on AutoDL.
- Keep GitHub focused on notes, small scripts, toy JSON/config files, summarized logs, and small screenshots or diagrams.
- Do not commit model weights, checkpoints, datasets, raw videos, external repository code, secrets, API keys, passwords, or private machine information.
