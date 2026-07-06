# ROCKET-1 Audit

This folder records a bounded ROCKET-1 repository and feasibility audit. It is not a full reproduction, not a training run, and not a claim of official Minecraft task success.

## Goal

Understand ROCKET-1's visual-temporal context prompting idea and identify what can realistically be demonstrated before research email outreach.

## Upstream Sources

| Item | Value |
| --- | --- |
| Paper | `https://arxiv.org/abs/2410.17856` |
| Project page | `https://craftjarvis.github.io/ROCKET-1/` |
| Official repository | `https://github.com/CraftJarvis/ROCKET-1.git` |
| Hugging Face paper page | `https://huggingface.co/papers/2410.17856` |
| Demo page | `https://huggingface.co/spaces/phython96/ROCKET-1-DEMO` |

## Repository Snapshot

| Item | Value |
| --- | --- |
| External path | `/root/autodl-tmp/external_repos/ROCKET-1` |
| Branch | `main` |
| Commit | `65cc70e5605a0e0a3b8ec74b52ed399a9b64e321` |
| Last commit summary | `65cc70e 2025-02-28 12:36:44 +0800 Update README.md` |

External repository code, checkpoints, datasets, raw videos, and large logs stay outside this GitHub repository.

## Main Finding

ROCKET-1 is a strong conceptual next step after DEPS and JARVIS-1 because it addresses a different bottleneck: language-only subgoal instructions lose spatial and interaction detail. The official system uses image input, segmentation masks, interaction IDs, and temporal memory to guide embodied Minecraft control.

The official demo path is not lightweight. It requires Python 3.10, OpenJDK 8, Minecraft/MCP-Reborn, ROCKET-1 model weights, SAM-2 segmentation code and checkpoints, rendering/system libraries, and GPU-compatible PyTorch.

## Local Demo

The paired toy demo lives in:

```text
experiments/rocket1-visual-prompt-demo/
```

It uses synthetic grid scenes to compare language-only instructions against mask/interaction prompts. This is a lightweight illustration of the idea, not official ROCKET-1 inference.
