# DEPS

## Reading Status

First lightweight reproduction pass completed on 2026-07-06.

## Problem

DEPS targets long-horizon planning in open-world Minecraft. Many goals require ordered prerequisite chains, environment interaction, and recovery when the world state does not match the plan. Simple examples such as obtaining an iron ingot already require wood, crafting, stone tools, a furnace, fuel, ore, and smelting.

## Core Idea

DEPS frames planning around four stages:

| Stage | Role |
| --- | --- |
| Describe | Convert the user objective and current state into a structured task description. |
| Explain | Reason about dependencies, missing prerequisites, and failure causes. |
| Plan | Generate a subgoal sequence that can be grounded in supported Minecraft actions. |
| Select | Choose the next executable subgoal based on the current plan and state. |

## Why LLM Planning Alone Is Not Enough

An LLM can propose plausible steps, but Minecraft execution requires more than plausible text:

- The plan must obey item, tool, and crafting constraints.
- Each subgoal must map to a supported controller skill.
- The simulator can invalidate assumptions through missing resources, mobs, terrain, time of day, or inventory changes.
- The agent needs feedback-driven replanning rather than a static one-shot plan.
- Long-horizon success depends on selecting the next feasible subgoal, not merely listing all desired steps.

## Upstream Implementation Inspected

| Item | Value |
| --- | --- |
| Repository | `https://github.com/CraftJarvis/MC-Planner.git` |
| Branch | `main` |
| Commit | `2a8b5a3e453c39634c2674d03e5ac21605270939` |
| Local external path | `/root/autodl-tmp/external_repos/MC-Planner` |
| Note | AutoDL `git clone` failed due GitHub transport/network errors; a GitHub source archive was unpacked under external storage for inspection. |

## What Was Reproduced Or Attempted

- Inspected the MC-Planner README, dependency file, main entry point, planner, and selector.
- Created a clean Conda environment named `mc-planner-test` with Python 3.10.
- Recorded the official setup requirements: modified MineDojo / MC-Simulator, MineCLIP, OpenAI keys, controller checkpoint, and Minecraft rendering.
- Created a lightweight DEPS-style planning demo for four tasks:
  - obtain wooden pickaxe
  - craft stone sword
  - obtain iron ingot
  - build a small shelter

## What Worked

- The official repository and commit were identified.
- The source tree was inspected outside our GitHub repository.
- Python 3.10 environment creation succeeded.
- The lightweight planning examples show dependency-aware decomposition and next-subgoal selection.

## What Failed Or Was Deferred

- AutoDL could not directly clone MC-Planner from GitHub during this pass.
- The official `main.py` demo was not run because it requires API keys, a controller checkpoint, modified simulator setup, and Minecraft rendering.
- Full dependency installation was deferred to avoid turning a short email-prep task into a long environment reproduction.

## What I Learned

- DEPS is best understood as an LLM planner connected to a grounded skill/controller layer, not as a standalone text planner.
- The Describe and Explain stages are useful for exposing hidden dependencies before execution.
- The Select stage is important because a full plan may include steps that are not executable yet.
- For a research email, a transparent planning-only reproduction is more credible than overclaiming a full simulator reproduction.

## Connection To JARVIS-1 And Later CraftJarvis Work

DEPS focuses on planning and subgoal selection, while JARVIS-1 and later CraftJarvis systems move toward more integrated multimodal agents, controllers, and Minecraft agent development infrastructure. DEPS helps define the high-level dependency reasoning problem that later systems must still solve when connecting language goals to visual observations and actions.

## Reproduction Angle

Use the current lightweight DEPS-style planning demo as a first evidence artifact. A deeper pass should only start after preparing OpenAI-compatible planner access, MC-Simulator, MineCLIP, controller checkpoints, and a short Minecraft runtime test plan under `/root/autodl-tmp`.
