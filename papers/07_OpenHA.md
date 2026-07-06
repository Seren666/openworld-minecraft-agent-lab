# OpenHA

## Reading Status

Superseded by `papers/07_OpenHA_CrossAgent.md`.

This placeholder is kept because the original repository scaffold included `papers/07_OpenHA.md`. The current email-ready note combines OpenHA with CrossAgent because the latest direction is action-space hierarchy plus dynamic cross-level action selection.

## Core Questions

- What hierarchy is used for planning, skills, and control?
- How does hierarchy improve open-world task execution?
- What assumptions are made about environment feedback and memory?

## Notes to Extract

- Hierarchical architecture
- Skill representation
- Planner-controller interface
- Evaluation tasks
- Failure modes

## Reproduction Angle

Map hierarchy choices onto the Minecraft task dependency graph and compare them with DEPS-style planning.

For the current bounded audit, see:

- `papers/07_OpenHA_CrossAgent.md`
- `docs/latest_direction_bridge.md`
