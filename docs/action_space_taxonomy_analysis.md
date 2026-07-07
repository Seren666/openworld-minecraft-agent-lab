# Action-Space Taxonomy Analysis for Minecraft Open-World Tasks

## Motivation

OpenHA and CrossAgent shift the Minecraft-agent question from only predicting an action to choosing the right action granularity. A long-horizon task may need high-level planning, memory/prerequisite reasoning, mid-level skills, visual grounding, and low-level control at different stages. This lightweight taxonomy asks which task types appear to depend on which interfaces.

This is a metadata-based and rule-based analysis. It is not official OpenHA/CrossAgent evaluation.

## Data Source

The analysis uses a local OpenHA repository snapshot outside this project repository.

| Field | Value |
| --- | --- |
| Upstream repository | `https://github.com/CraftJarvis/OpenHA` |
| Branch | `main` |
| Commit | `606efc69e945bd02c700e584136bcc105d22f122` |
| Local source type | GitHub zip snapshot inspected outside this repository |
| Main metadata source | `CrossAgent/STRL/data_processor/task_suc_rate.json` |
| Additional task source | `CrossAgent/STRL/data_processor/utils/task_list.json` and rollout-debug task directory names |
| Scope | full local metadata-derived task names plus bounded representative additions |

The structured metadata provided 1192 unique task names from `task_suc_rate.json`, 30 tasks from `task_list.json`, and 9 inferred rollout-debug task names. After de-duplication and adding representative tasks for shelter, cave exploration, furnace use, and long-horizon obtain examples, the final taxonomy artifact covers 1200 task rows and 1200 unique task names.

## Method

The script `experiments/openha-action-space-analysis/analyze_openha_tasks.py` classifies task names with transparent rules. It does not import OpenHA code or run Minecraft.

Each task is assigned:

- one task category
- one or more preferred action/interface labels
- required information types
- likely failure mode under a fixed action space

The labels are intentionally cautious. They are designed to surface action-space pressure, not to estimate official success rate.

## Quantitative Summary

### Row And Unique-Task Accounting

| Statistic | Value |
| --- | ---: |
| Total task rows | 1200 |
| Unique task names | 1200 |
| Duplicate task names | 0 |
| Extra rows from duplicate task names | 0 |

Duplicates do not exist in the final taxonomy CSV. Some upstream sources overlap conceptually because `task_suc_rate.json`, `task_list.json`, rollout-debug directory names, and bounded representative additions can describe similar Minecraft task families, but the analysis script de-duplicates exact task names before writing `task_taxonomy.csv`.

All percentages in the category and interface tables below are computed over task rows. In the current artifact, this is numerically equivalent to percentages over unique task names because each row has a unique `task_name`.

### Category Distribution

| Category | Task count | Percentage |
| --- | ---: | ---: |
| mining | 328 | 27.3% |
| tool_use_or_interaction | 240 | 20.0% |
| crafting | 238 | 19.8% |
| building_or_shelter | 227 | 18.9% |
| smelting_or_cooking | 63 | 5.2% |
| combat | 63 | 5.2% |
| long_horizon_obtain | 39 | 3.2% |
| navigation_or_exploration | 1 | 0.1% |
| mixed_or_unknown | 1 | 0.1% |

### Interface Pressure

Percentages can sum above 100% because a task can require multiple interfaces.

| Preferred interface | Task count | Percentage |
| --- | ---: | ---: |
| mid_level_skill_action | 1135 | 94.6% |
| memory_or_prerequisite_reasoning | 851 | 70.9% |
| visual_grounding_or_mask_action | 737 | 61.4% |
| low_level_control | 658 | 54.8% |
| high_level_planning | 569 | 47.4% |
| dynamic_action_space_switching | 463 | 38.6% |

## Key Observations

- Different Minecraft task types favor different action granularities. A single fixed action representation is likely too rigid across mining, crafting, smelting, combat, building, and long-horizon obtain tasks.
- Crafting and smelting tasks often depend on recipe/prerequisite and inventory state. They are less about raw controller movement and more about valid staged preconditions.
- Mining, combat, navigation, and building tasks often need visual grounding and low-level control because the agent must localize objects, aim, place, move, or react.
- Long-horizon obtain tasks likely need dynamic action-space switching because they combine planning, memory, visual grounding, skill execution, and low-level control.
- A useful research direction is not just "which action is next?" but "which action interface should be active at this task stage?"

## Preliminary Research Questions

1. Could memory or failure traces help select the next action interface, not only the next action?
2. Could task-stage-aware action costs improve Multi-Turn GRPO or related post-training for Minecraft agents?
3. Could world models or diffusion-based imagined rollouts help evaluate action-interface choices before real execution?

## Limitations

- This is not official OpenHA or CrossAgent evaluation.
- No model training was run.
- No checkpoint inference was run.
- The taxonomy is rule-based and preliminary.
- Task names and public metadata do not fully reveal trajectory difficulty, inventory state, world layout, or visual ambiguity.
- Representative additions are bounded and are used only to cover task types missing from the local structured metadata.

## Next Steps

- Add trajectory-level failure analysis when safe summarized traces are available.
- Diagnose benchmark tasks by action-interface pressure rather than only by success/failure.
- Annotate task stages with action-space switching decisions.
- Explore memory-conditioned interface selection.
- Compare whether world-model-assisted rollouts can predict bad action-interface choices before real execution.
