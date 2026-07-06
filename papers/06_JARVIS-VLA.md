# JARVIS-VLA

## Reading Status

Bounded paper/repository audit and lightweight action-interface demo completed on 2026-07-06.

## Problem

Large VLMs have useful visual and language knowledge, but they are not directly action-capable. A Minecraft agent needs more than a text answer: it needs executable keyboard/mouse-style actions grounded in the current visual state, inventory, task instruction, and action space.

The core problem is converting visual-language understanding into structured game control.

## Core Idea

JARVIS-VLA post-trains large-scale vision-language models to play visual games with keyboard and mouse actions. The high-level interface is:

```text
visual observation + language instruction + state/history -> structured game action
```

In Minecraft-like settings, this means an action prediction system must choose actions such as moving, turning, attacking/mining, using a station, crafting, equipping tools, placing blocks, waiting, or retreating.

## Why Action Representation Matters

Action representation is a central design choice. The same high-level instruction can require different immediate actions:

- "collect wood" -> attack a visible tree trunk
- "craft sticks" -> use a crafting table, then choose a recipe
- "smelt iron" -> use a furnace, not mine or craft
- "obtain iron ore" with only a wooden pickaxe -> do not mine yet
- "survive" at night with a visible mob -> retreat, block, or fight based on state

This is why VLA-style action prediction differs from pure high-level planning. The output must be executable by the game controller.

## Relationship To DEPS, JARVIS-1, And ROCKET-1

- DEPS focuses on high-level task decomposition and failure-aware planning.
- JARVIS-1 connects multimodal perception, memory, planning, and embodied control.
- ROCKET-1 highlights target grounding through visual masks and interaction types.
- JARVIS-VLA focuses on the action interface: turning visual-language context into concrete keyboard/mouse control.

Together, these papers form a path from planning, to memory, to visual grounding, to action prediction.

## Upstream Implementation Inspected

| Item | Value |
| --- | --- |
| Paper title | `JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse` |
| Paper | `https://arxiv.org/abs/2503.16365` |
| Project page | `https://craftjarvis.github.io/JarvisVLA/` |
| Repository | `https://github.com/CraftJarvis/JarvisVLA.git` |
| Models collection | `https://huggingface.co/collections/CraftJarvis/jarvis-vla-v1-67dc157a99d011efd7d7f7e4` |
| Dataset | `https://huggingface.co/datasets/CraftJarvis/minecraft-vla-sft` |
| Branch | `master` |
| Commit | `0aafd2ed0ba9270f40d710440ca70cdc3fa48a11` |
| AutoDL external path | `/root/autodl-tmp/external_repos/JarvisVLA` |

## What We Audited

- README installation and inference path.
- `requirements.txt`.
- evaluation shell scripts for kill, mine, craft, and smelt tasks.
- vLLM serving path.
- dataset and model links.
- safe syntax compilation for a bounded subset of Python files.
- current Blackwell PyTorch CUDA 12.8 environment suitability for small GPU checks.

## What Worked

- Official repository cloned successfully under `/root/autodl-tmp/external_repos`.
- Branch and commit were recorded.
- A bounded Python syntax smoke test passed.
- The existing data-disk PyTorch environment (`torch 2.11.0+cu128`) was confirmed to see the Blackwell GPU.
- A toy VLA action-interface demo was created.
- A tiny GPU-backed toy action scorer ran one forward pass on the Blackwell GPU.

## What Can Be Realistically Reproduced In A Bounded Pass

Short term:

- Repository audit and setup feasibility report.
- Toy action-interface demo mapping observations and instructions to structured actions.
- Tiny GPU-backed scoring demo for infrastructure evidence.
- Comparison with DEPS/JARVIS-1/ROCKET-1 interfaces.

Medium term:

- Install JARVIS-VLA in a data-disk environment.
- Use vLLM only after model size, storage, and GPU memory are controlled.
- Try a very short single-task rollout only after MineStudio, rendering, and logs are safely configured under `/root/autodl-tmp`.

## What Remains Blocked

- Official model weights were not downloaded.
- The Minecraft VLA SFT dataset was not downloaded.
- vLLM serving was not started.
- MineStudio simulator was not launched.
- No training, fine-tuning, rollout, raw video, or large log generation was run.
- Official reproduction remains blocked by model size, dataset assets, MineStudio setup, rendering, and evaluation runtime.

## Reproduction Angle

The honest reproduction angle is a lightweight action-interface demo. It shows the key abstraction of JARVIS-VLA without claiming official model behavior: visual-language input plus state and an action schema can produce a structured low-level action, while pure language planning remains too abstract for control.
