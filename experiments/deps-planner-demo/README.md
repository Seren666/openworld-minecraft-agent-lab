# DEPS Planner Demo

This experiment tracks a lightweight planner-only reproduction inspired by DEPS.

## Goal

Convert a high-level Minecraft objective into a dependency-aware task plan, using prompts and small hand-written examples before attempting any environment integration.

## Planned Components

- Prompt examples under `prompts/`
- Markdown run summaries under `logs/`
- Small screenshots under `screenshots/`
- A simple task graph format for planning notes

## First Demo Target

Input: `Obtain an iron pickaxe from a new survival world.`

Expected output:

- Required resources
- Ordered subtasks
- Dependency graph
- Likely failure cases
