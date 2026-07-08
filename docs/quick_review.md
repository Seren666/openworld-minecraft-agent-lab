# Quick Review

## What This Repository Is

This is an unofficial student research record for open-world Minecraft agents. It contains paper notes, repository audits, lightweight demos, bounded feasibility checks, and careful documentation of blockers.

It is designed to show what was inspected and tested, while keeping large assets, external repository code, datasets, checkpoints, raw videos, and secrets out of Git.

## Main Research Story

The repository follows this chain:

```text
planning -> memory -> visual grounding -> action representation -> action-space learning
```

DEPS / MC-Planner motivates dependency-aware planning. JARVIS-1 adds memory as a way to reduce repeated long-horizon mistakes. ROCKET-1 highlights visual and temporal grounding. JARVIS-VLA shifts the interface toward executable action prediction. OpenHA and CrossAgent move the question toward hierarchical action spaces: when should an agent use a high-level skill, a mid-level structured action, or low-level control?

## Most Relevant Artifacts

- [Action-space taxonomy analysis](action_space_taxonomy_analysis.md): Exploratory OpenHA/CrossAgent metadata/config-based task taxonomy, including source-scope clarification, local row accounting, failure-mode observations, and a 100-record manual sanity-check sample.
- [MineStudio smoke test](minestudio_smoke_test.md): Bounded package install/import and simulator-readiness check. Package-level import passed; `cv2` and Java blockers were resolved; simulator/rollout remains blocked by `torch` plus DISPLAY/Xvfb runtime support.
- [Reproduction summary](reproduction_summary.md): Compact status table covering paper audits, toy demos, blocked official systems, and evidence-supported scope.
- [Latest direction bridge](latest_direction_bridge.md): Bridge from planning, memory, grounding, and VLA action prediction toward OpenHA/CrossAgent, GRPO-style post-training, and world-model-based agent learning.
- [Four-interface comparison](four_interface_comparison.md): Side-by-side comparison of planning, memory, visual grounding, and action representation interfaces on shared Minecraft task examples.

## What Can Be Discussed

- Why fixed action spaces may be insufficient for long-horizon Minecraft tasks.
- Why task-name-only taxonomy is useful for a first pass but limited by missing trajectory, inventory, visual, and world-state information.
- Why trajectory outcomes, failure traces, inventory state, visibility, and action history could help diagnose when to switch action spaces.
- What MineStudio blockers were found before any serious simulator, benchmark, or rollout work.
- How lightweight demos can clarify interfaces without relying on large checkpoints or long training runs.

## What Is Not Claimed

- No paper-author benchmark run is reported.
- No model training is reported.
- No checkpoint inference is reported.
- No official Minecraft evaluation result is reported.
- No complete MineStudio simulator rollout is reported.
- No large weights, datasets, checkpoints, raw videos, external repository code, credentials, or private machine details are committed.
