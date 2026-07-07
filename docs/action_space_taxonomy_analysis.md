# Action-Space Taxonomy Analysis for Minecraft Open-World Tasks

## Motivation

OpenHA and CrossAgent shift the Minecraft-agent question from only predicting an action to choosing the right action granularity. A long-horizon task may need high-level planning, memory/prerequisite reasoning, mid-level skills, visual grounding, and low-level control at different stages. This lightweight taxonomy asks which task types appear to depend on which interfaces.

This is an exploratory, metadata/config-based, rule-based analysis. It is not official OpenHA/CrossAgent evaluation, and it does not report the official benchmark size.

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
| Scope | local metadata/config-derived task-name records plus bounded representative additions |

The OpenHA/CrossAgent paper framing describes an over-800-task benchmark. The 1200 records in this repository are not presented as that official benchmark size. They are local unique task-name records parsed from public metadata/config outputs plus bounded representative additions.

## Source Breakdown

| Source path | Source type | Raw unique names found | Final rows mentioning source | Exclusive new rows after exact-name de-duplication | Entry interpretation |
| --- | --- | ---: | ---: | ---: | --- |
| `CrossAgent/STRL/data_processor/task_suc_rate.json` | CrossAgent metadata/config summary | 1192 | 1192 | 1162 | task-name records / atomic or config-level task variants, not the official benchmark-size denominator |
| `CrossAgent/STRL/data_processor/utils/task_list.json` | CrossAgent task-list/config file | 30 | 30 | 0 | task-list entries that overlap with `task_suc_rate.json` in this snapshot |
| rollout-debug directory names | generated/debug directory labels | 9 | 9 | 0 | directory-derived task labels that overlap with config metadata; not new benchmark tasks |
| `manual_representative_sample` | manually added analysis sample | 8 | 8 | 8 | bounded Minecraft examples added only to cover readable task types such as shelter, cave exploration, and furnace use |

### Final Row-Source Combinations

| Final `source` value in `task_taxonomy.csv` | Row count |
| --- | ---: |
| `CrossAgent/STRL/data_processor/task_suc_rate.json` | 1162 |
| `CrossAgent/STRL/data_processor/utils/task_list.json; CrossAgent/STRL/data_processor/task_suc_rate.json` | 21 |
| `CrossAgent/STRL/data_processor/utils/task_list.json; CrossAgent/STRL/data_processor/task_suc_rate.json; rollout_debug directory names` | 9 |
| `manual_representative_sample` | 8 |

The final union contains 1200 unique task-name records. The row count is larger than the paper-level over-800-task benchmark framing because the local metadata/config files include atomic names and config-level variants. Source counts should not be summed as an official benchmark count.

## Method

The script `experiments/openha-action-space-analysis/analyze_openha_tasks.py` classifies task names with transparent rules. It does not import OpenHA code or run Minecraft.

Each task is assigned:

- one task category
- one or more preferred action/interface labels
- required information types
- likely failure mode under a fixed action space

The labels are intentionally cautious. They are designed to surface action-space pressure, not to estimate official success rate.

## Main Findings

- The taxonomy is useful as a task-interface pressure map, not as an official benchmark statistic.
- The local records suggest that Minecraft tasks pressure different action granularities: recipe-like tasks lean toward prerequisite and inventory reasoning, while mining, combat, building, and navigation-like tasks lean more toward visual grounding and low-level control.
- Dynamic action-space switching appears to be relevant for a meaningful subset of local records, but it should not be treated as universally required for every task.
- The most useful next step is trajectory-level failure analysis, because task names alone cannot reveal full world state, inventory state, or visual ambiguity.

## Detailed Exploratory Statistics

### Row And Unique-Task Accounting

| Statistic | Value |
| --- | ---: |
| Total task rows | 1200 |
| Unique task names | 1200 |
| Duplicate task names | 0 |
| Extra rows from duplicate task names | 0 |

Duplicates do not exist in the final taxonomy CSV. Some upstream sources overlap conceptually because `task_suc_rate.json`, `task_list.json`, rollout-debug directory names, and bounded representative additions can describe similar Minecraft task families, but the analysis script de-duplicates exact task names before writing `task_taxonomy.csv`.

All percentages in the category and interface tables below are computed over local task-name rows. In the current artifact, this is numerically equivalent to percentages over unique task names because each row has a unique `task_name`. These percentages should be interpreted as exploratory metadata/config statistics, not official benchmark results.

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

- Different Minecraft task types appear to favor different action granularities. A single fixed action representation is likely too rigid across mining, crafting, smelting, combat, building, and long-horizon obtain tasks.
- Crafting and smelting tasks often appear to depend on recipe/prerequisite and inventory state. They are less about raw controller movement and more about valid staged preconditions.
- Mining, combat, navigation, and building tasks often appear to need visual grounding and low-level control because the agent must localize objects, aim, place, move, or react.
- Long-horizon obtain tasks are likely candidates for dynamic action-space switching because they combine planning, memory, visual grounding, skill execution, and low-level control.
- A useful research direction is not just "which action is next?" but "which action interface should be active at this task stage?"

## Manual Sanity Check

The folder includes a 100-record stratified sanity-check sample:

- `experiments/openha-action-space-analysis/results/manual_check_sample_100.csv`
- `experiments/openha-action-space-analysis/results/manual_check_protocol.md`

This sample uses conservative first-pass manual labels and confidence notes. It is not a validation result and does not report agreement. Its purpose is to expose likely ambiguity in task-name-only classification, especially for config-style names where the command prefix and object semantics can imply different categories.

## Preliminary Research Questions

1. Could memory or failure traces help select the next action interface, not only the next action?
2. Could task-stage-aware action costs improve Multi-Turn GRPO or related post-training for Minecraft agents?
3. Could world models or diffusion-based imagined rollouts help evaluate action-interface choices before real execution?

## Limitations

- This is not official OpenHA or CrossAgent evaluation.
- No model training was run.
- No checkpoint inference was run.
- The taxonomy is rule-based and preliminary.
- The 1200 local task-name records are not the official over-800-task benchmark size described in the OpenHA/CrossAgent paper framing.
- Task names and public metadata do not fully reveal trajectory difficulty, inventory state, world layout, or visual ambiguity.
- Representative additions are bounded and are used only to cover task types missing from the local structured metadata.

## Next Steps

- Add trajectory-level failure analysis when safe summarized traces are available.
- Diagnose benchmark tasks by action-interface pressure rather than only by success/failure.
- Annotate task stages with action-space switching decisions.
- Explore memory-conditioned interface selection.
- Compare whether world-model-assisted rollouts can predict bad action-interface choices before real execution.
