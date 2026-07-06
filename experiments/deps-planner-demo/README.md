# DEPS / MC-Planner Lightweight Reproduction

This folder records a lightweight DEPS-style reproduction for Minecraft planning. It is not an official reproduction and does not claim to reproduce the full DEPS paper, controller, simulator, or benchmark results.

## What DEPS Is

DEPS stands for Describe, Explain, Plan, and Select. At a high level, DEPS uses a large language model to reason about long-horizon Minecraft tasks, then connects those plans to a controller that can execute supported subtasks in a Minecraft simulator.

The relevant upstream implementation inspected for this pass is:

| Item | Value |
| --- | --- |
| Upstream repository | `https://github.com/CraftJarvis/MC-Planner.git` |
| Branch | `main` |
| Commit | `2a8b5a3e453c39634c2674d03e5ac21605270939` |
| Local external path | `/root/autodl-tmp/external_repos/MC-Planner` |
| Source retrieval note | `git clone` was blocked by GitHub transport errors on AutoDL, so a GitHub source archive from `main` was unpacked under external storage for inspection. |

## Why Long-Horizon Minecraft Planning Is Hard

Minecraft tasks often require many dependent steps. For example, an iron ingot requires wood, tools, stone, a furnace, fuel, iron ore, and smelting. A planner must reason about prerequisites, tool constraints, inventory state, failure recovery, and the difference between strict dependencies and optional preparation.

LLM planning alone is not enough because the generated plan still needs:

- Grounding in Minecraft item and crafting rules
- A supported controller action or skill for each subgoal
- Environment feedback when assumptions fail
- A way to select the next executable subgoal from several candidates
- Recovery when a task is infeasible in the current state

## What This Demo Tries To Show

This lightweight DEPS-style planning demo focuses on the planning record, not Minecraft execution. It demonstrates whether we understand the paper's planning loop well enough to produce useful email evidence:

- Decompose a task into dependencies.
- Explain why each prerequisite matters.
- Produce an ordered plan that can be checked by a human.
- Select the next executable action based on current inventory and blockers.

## Four Stages

| Stage | Lightweight interpretation |
| --- | --- |
| Describe | Restate the goal, current assumptions, needed objects, tools, and environment facts. |
| Explain | Explain dependencies and why each prerequisite must happen before later steps. |
| Plan | Produce an ordered subgoal list with inputs, outputs, and likely blockers. |
| Select | Pick the next executable subgoal from the plan given the current state. |

## Example Tasks

- Obtain wooden pickaxe
- Craft stone sword
- Obtain iron ingot
- Build a small shelter

Detailed examples are in `task_examples.md`.

## Logs Collected

The run log records:

- Upstream repository URL, branch, and commit
- AutoDL external path
- README and dependency observations
- Conda setup attempt
- Why the official MC-Planner demo was not run end-to-end
- A planning-only local demonstration for the four example tasks

Large raw logs, external source code, controller checkpoints, datasets, videos, and model weights are not committed.

## Success and Failure Criteria

Success for this pass means:

- The official MC-Planner repository is identified and inspected.
- Setup requirements and blockers are documented.
- A clean planning-only DEPS-style record is produced for multiple Minecraft tasks.
- The record is useful for a research email without overstating reproduction completeness.

Failure or blocker conditions include:

- Missing OpenAI API keys
- Missing controller checkpoint
- Missing modified MineDojo / MC-Simulator setup
- GitHub clone transport errors
- Any dependency installation path that would turn this into a long setup instead of a short evidence-gathering pass
