# Roadmap

This roadmap is intentionally practical and email-oriented. The goal is to show preparation, judgment, and a clear research direction before attempting expensive official training or evaluation.

## Current Story

The repository now compares four interfaces for Minecraft open-world agents:

```text
DEPS planning -> JARVIS-1 memory -> ROCKET-1 visual grounding -> JARVIS-VLA action prediction
```

The immediate aim is to make this story clear enough for advisor outreach.

## Next Steps Before Email

1. Polish paper notes and make terminology consistent across `papers/`.
2. Add a GROOT reading note focused on video instruction, goal representation, and open-ended behavior.
3. Add an OmniJARVIS reading note focused on unified VLA tokenization and generalist Minecraft control.
4. Optionally add an OpenHA reading note focused on action space, hierarchy, and evaluation design.
5. Add one compact diagram or table that links planning, memory, visual grounding, and action prediction.

## If An Advisor Responds

Choose one focused direction instead of starting large training immediately:

| Direction | Possible student-scale work |
| --- | --- |
| Benchmark evaluation | Define a small task set and compare failure modes across interfaces. |
| Memory retrieval analysis | Study when retrieved memory helps or hurts long-horizon planning. |
| Failure case analysis | Build a taxonomy for tool, recipe, spatial, and action-selection failures. |
| Visual prompt interface | Extend the ROCKET-1 toy demo into more structured mask/affordance examples. |
| Action space comparison | Compare discrete action schemas for Minecraft-style VLA control. |

## Deferred Until There Is A Clear Research Direction

- Full official model training.
- Large checkpoint or dataset downloads.
- Long Minecraft rollout jobs.
- Multi-GPU experiments.
- Large video generation.

## Engineering Rules

- Keep external repositories, environments, caches, logs, checkpoints, datasets, and temporary files under `/root/autodl-tmp` on AutoDL.
- Keep GitHub focused on notes, small scripts, toy JSON/config files, summarized logs, and small screenshots or diagrams.
- Do not commit model weights, checkpoints, datasets, raw videos, external repository code, secrets, API keys, passwords, or private machine information.
