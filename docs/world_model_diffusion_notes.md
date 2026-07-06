# World Model And Diffusion Notes

This is a concise next-reading note. It is not a reproduction log.

## What Is A World Model?

A world model is a learned predictive model of the environment. Given observations, actions, and history, it estimates what may happen next.

For embodied agents, a useful world model can answer questions such as:

- What will the agent see after this action?
- Will this plan likely fail before reaching the goal?
- Which future states are reachable from the current state?
- Can we train or evaluate policies using imagined rollouts?

## Why Diffusion And Video Diffusion Matter

Minecraft is visual, temporal, and open-ended. Text-only state summaries lose details such as object layout, tool position, terrain, occlusion, and motion.

Diffusion and video diffusion models are relevant because they can model possible future frames or trajectories. For open-world agents, this suggests a path from passive visual generation toward predictive simulation.

## How World Models Could Help Minecraft Agents

| Use case | Why it matters |
| --- | --- |
| Imagined rollouts | Test candidate plans before executing them in Minecraft. |
| Failure prediction | Detect that a plan is likely to fail because of missing tools, bad terrain, or unreachable targets. |
| Data generation | Create additional visual/task situations for rare or expensive cases. |
| Safer RL | Reduce wasted or risky simulator interactions by pretraining or filtering in a learned model. |
| Planning | Score future consequences, not only current language plans. |

## Connection To This Repository

The current story is:

```text
planning -> memory -> visual grounding -> action prediction -> dynamic action-space selection
```

World models add a predictive layer:

```text
What future states are likely if the agent chooses this action or action space?
```

This could connect DEPS-style planning, ROCKET-1-style visual grounding, JARVIS-VLA-style action prediction, and OpenHA/CrossAgent action-space selection.

## Reading Direction

Before attempting any implementation, the practical next step is reading and comparison:

- world models for agents
- video diffusion as predictive simulation
- model-based RL with imagined rollouts
- Minecraft or open-world environments as stress tests for predictive models

This repository does not claim a world-model reproduction. The purpose of this note is to identify why world/diffusion models are a relevant next research direction after OpenHA/CrossAgent.
