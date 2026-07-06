# OpenHA And CrossAgent Notes

This is a research-preparation note, not an official reproduction.

## Source

- OpenHA repository: https://github.com/CraftJarvis/OpenHA
- Branch audited: `main`
- Commit audited: `606efc69e945bd02c700e584136bcc105d22f122`
- CrossAgent folder: present at `CrossAgent/`, with `MTRL/`, `SFT/`, and `STRL/` subfolders
- OpenHA paper: https://arxiv.org/abs/2509.13347
- CrossAgent paper: https://arxiv.org/abs/2512.09706

## Problem

No single Minecraft action space is universally optimal.

High-level actions can express long-horizon intent, but they hide important control details. Low-level keyboard/mouse actions are expressive, but they make long-horizon exploration and credit assignment difficult. Mid-level action abstractions can help, but they may fail when a task needs a different level of precision.

The key research problem is:

```text
How should an embodied agent choose the right action abstraction for the current state, task, and horizon?
```

## Core Idea Of OpenHA

OpenHA treats hierarchical action spaces as the central object of study. Instead of assuming one action interface, it compares and organizes multiple levels of action abstraction in Minecraft.

The important idea for this repository is Chain of Action: an agent can reason across a hierarchy, connecting high-level goals to lower-level executable behavior. This directly extends earlier VLA-interface work, where the main question was which action to predict next.

## Core Idea Of CrossAgent

CrossAgent moves from comparing action spaces to dynamically selecting across heterogeneous action spaces. The goal is one agent that can decide when to use a high-level skill, a mid-level structured action, or a lower-level control action.

The OpenHA repository contains a `CrossAgent/` folder with `MTRL/`, `SFT/`, and `STRL/` subfolders, indicating a training pipeline around supervised fine-tuning and reinforcement/post-training style methods.

The official README lists CrossAgent model and dataset assets on Hugging Face, including SFT and GRPO-related datasets. This repository records their existence only and does not download or train on them.

## Why GRPO Matters

SFT can teach the model how expert-like actions are formatted and distributed, but Minecraft progress depends on long-horizon outcomes. GRPO-style post-training is relevant because it can optimize policy behavior from grouped rollout feedback.

For CrossAgent, the interesting question is not only "which action is next?" but also:

```text
Which action level should be selected, and did that level help task progress?
```

This repository has not trained CrossAgent with GRPO. The contribution here is identifying GRPO-based post-training as a likely next concept to study for dynamic action-space selection.

## Connection To Existing Demos

The current repository story becomes:

```text
DEPS planning -> JARVIS-1 memory -> ROCKET-1 visual mask -> JARVIS-VLA action prediction -> OpenHA/CrossAgent dynamic action-space selection
```

| Existing component | What it contributes | Remaining gap OpenHA/CrossAgent addresses |
| --- | --- | --- |
| DEPS planning | Dependency-aware subgoals | Does not decide the best action abstraction. |
| JARVIS-1 memory | Past task knowledge and failure reminders | Memory can suggest what to do, but not how granular the next action should be. |
| ROCKET-1 visual mask | Spatial target grounding | Grounding identifies the target, but not the control interface. |
| JARVIS-VLA action prediction | Mapping observation and instruction to action | A fixed action interface may not fit every task phase. |
| OpenHA/CrossAgent | Hierarchical and dynamic action-space selection | Official reproduction requires heavier infrastructure. |

## What Was Attempted Here

- Located and audited the official OpenHA repository.
- Recorded branch and commit hash.
- Confirmed the presence of `CrossAgent/` material in the repository.
- Summarized README-level installation and asset requirements.
- Connected OpenHA/CrossAgent to this repository's prior planning, memory, grounding, and action-interface demos.

## What Is Lightweight Feasible

- Write an action-space comparison table for Minecraft tasks.
- Build a toy action selector that chooses among high-level, mid-level, and low-level actions.
- Compare failure modes when the wrong action abstraction is selected.
- Extend the JARVIS-VLA toy action demo with an action-level selector.

## What Remains Blocked Or Deferred

- Official OpenHA rollout in Minecraft.
- Official CrossAgent SFT or GRPO training.
- Large model checkpoint downloads.
- Large dataset downloads.
- Long simulator jobs or Minecraft evaluation.
- Multi-GPU model serving commands from the official README.

## Takeaway

OpenHA and CrossAgent are important because they shift the research question from "how do we plan or predict an action?" to "which action space should the agent use, and how can post-training improve that choice?"
