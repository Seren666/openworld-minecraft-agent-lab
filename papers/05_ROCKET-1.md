# ROCKET-1

## Reading Status

Bounded repository audit and lightweight visual prompt demo completed on 2026-07-06.

## Problem

Language-only subgoal instructions lose spatial detail. In Minecraft, an instruction such as "mine the tree", "use the station", or "go inside" can be ambiguous because the scene may contain multiple valid objects and multiple possible affordances.

For embodied agents, this ambiguity is costly. A wrong spatial target can waste time, destroy blocks, use the wrong crafting station, or break the task dependency chain.

## Core Idea

ROCKET-1 introduces visual-temporal context prompting for open-world Minecraft interaction. Instead of using language alone, the policy receives:

- the current visual observation
- a segmentation mask that highlights the target region
- an interaction type, such as mine, interact, craft, switch, hunt, or approach
- temporal context or memory from previous steps

The mask communicates where to act. The interaction type communicates how to act. The temporal context helps the policy maintain or switch targets across frames.

## How Masks Help

Segmentation masks are useful because they carry spatial and affordance information that a short text instruction may omit. For example:

- "mine the tree" becomes a specific highlighted tree plus `Mine`
- "use the station" becomes the furnace mask plus `Interact`
- "now mine the ore" can switch the mask from stone to iron ore
- "get inside" can highlight the door rather than the wall

This is especially relevant in Minecraft because many objects are visually similar, nearby objects can share names or roles, and interaction success depends on the correct tool, view direction, distance, and action type.

## Relationship To DEPS And JARVIS-1

DEPS focuses on high-level planning, dependency reasoning, and failure recovery. JARVIS-1 adds multimodal perception, memory, planning, and embodied control. ROCKET-1 addresses a lower-level but critical interface problem: how to tell the controller which visible object to interact with and how.

In this project:

- DEPS motivates subgoal structure.
- JARVIS-1 motivates memory-augmented multimodal planning.
- ROCKET-1 motivates mask-guided interaction and visual-temporal prompting.

Together, they form a useful research path from symbolic planning to memory to embodied visual control.

## Upstream Implementation Inspected

| Item | Value |
| --- | --- |
| Paper | `https://arxiv.org/abs/2410.17856` |
| Project page | `https://craftjarvis.github.io/ROCKET-1/` |
| Repository | `https://github.com/CraftJarvis/ROCKET-1.git` |
| Branch | `main` |
| Commit | `65cc70e5605a0e0a3b8ec74b52ed399a9b64e321` |
| AutoDL external path | `/root/autodl-tmp/external_repos/ROCKET-1` |

The official README notes that ROCKET-1 was accepted by CVPR 2025 and that a MineStudio implementation is also available.

## What We Audited

- README, installation path, usage snippet, and interaction types.
- Root `pyproject.toml` dependency list.
- `rocket/realtime_sam` setup files and SAM-2 checkpoint script.
- Candidate demo and evaluation scripts, including `rocket/arm/eval_rocket.py`.
- Minecraft simulator requirement through MCP-Reborn.
- Model and checkpoint requirements from Hugging Face.
- Whether a minimal official demo looked safe to run as a bounded feasibility check.

## What Worked

- The official repository cloned successfully under `/root/autodl-tmp/external_repos`.
- Branch and commit were recorded.
- `rocket/arm/eval_rocket.py` and `rocket/stark_tech/env_interface.py` passed Python syntax compilation.
- A separate Blackwell-compatible PyTorch test succeeded with `torch 2.11.0+cu128`, which supports `sm_120`.
- A lightweight original visual prompt demo was created under `experiments/rocket1-visual-prompt-demo/`.

## What Can Be Realistically Reproduced In A Bounded Pass

Short term:

- Repository audit and feasibility report.
- Explanation of visual-temporal context prompting.
- Lightweight synthetic grid demo comparing language-only prompts against mask/interaction prompts.
- Small SVG assets and Markdown logs showing ambiguity and target disambiguation.

Medium term:

- Install ROCKET-1 and realtime SAM in a Blackwell-compatible PyTorch environment.
- Download only the smallest required SAM-2 checkpoint if the target demo needs it.
- Load model weights under `/root/autodl-tmp` if the checkpoint size and authentication requirements are acceptable.
- Try the Gradio or inference path under a short timeout after simulator and rendering are controlled.

## What Remains Blocked

- ROCKET-1 model weights were not downloaded.
- SAM-2 checkpoints were not downloaded.
- MCP-Reborn simulator was not downloaded or launched.
- System rendering libraries were not installed during this sprint.
- No Minecraft environment, Gradio demo, or live policy inference was run.
- The official dependency stack overlaps with known MineStudio/JARVIS blockers: OpenCV, `av`, gym variants, Java, Minecraft rendering, and large assets.

## Reproduction Angle

The honest reproduction angle is a visual prompt concept demo, not full ROCKET-1 execution. The toy demo shows why mask-guided prompts can be stronger than language-only instructions for spatially grounded Minecraft interaction.
