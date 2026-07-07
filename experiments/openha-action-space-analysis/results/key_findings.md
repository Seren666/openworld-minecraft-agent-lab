# Key Findings

This is a preliminary, exploratory taxonomy over OpenHA/CrossAgent public metadata/config-derived task-name records plus a bounded representative sample. It is not official model evaluation.

The OpenHA/CrossAgent paper framing describes an over-800-task benchmark. The 1200 records here are local unique task-name records parsed from public metadata/config outputs plus bounded additions, not the official benchmark size.

## Strongest Findings

1. **The local artifact contains 1200 task-name rows and 1200 unique task names.** This should be read as an exploratory metadata/config scope, not as the official OpenHA benchmark denominator.
2. **Most records come from CrossAgent metadata/config outputs.** The final CSV includes 8 bounded representative samples; the remaining records are parsed from public OpenHA/CrossAgent files.
3. **The taxonomy suggests that Minecraft task families place different pressure on action granularity.** Crafting and smelting lean toward prerequisite/inventory reasoning, while mining, combat, building, and navigation lean more toward visual grounding or low-level control.
4. **Dynamic action-space switching appears as a meaningful subset rather than a universal requirement.** This supports asking when to switch action interfaces, not only which next action to predict.

## Detailed Exploratory Statistics

- `crafting` accounts for 238 local records (19.8% of rows).
- `dynamic_action_space_switching` is assigned to 463 local records (38.6% of rows).
- `memory_or_prerequisite_reasoning` appears in 851 local records (70.9% of rows).
- `visual_grounding_or_mask_action` appears in 737 local records (61.4% of rows).

Percentages are computed over local task-name rows. In this artifact, row-level and unique-task percentages are identical because the final CSV has no duplicate exact task names.

## Manual Sanity Check

- A 100-record stratified sample is provided in `manual_check_sample_100.csv`.
- The sample uses first-pass conservative manual labels and confidence notes.
- This is a qualitative sanity check, not a validation result.
- Agreement is not reported because labels were not adjudicated by independent annotators and no trajectory-level ground truth was used.

## Cautious Hypotheses

- Long-horizon obtain tasks may benefit from memory-conditioned action-space selection.
- Crafting and smelting tasks appear more dependent on prerequisite and inventory state than on raw low-level control alone.
- Mining, combat, navigation, and building tasks appear more dependent on visual grounding and low-level control than recipe-only tasks.

## Limitations

- The taxonomy is rule-based and preliminary.
- Task names and public metadata may not reveal full trajectory difficulty.
- No official OpenHA/CrossAgent checkpoint inference or Minecraft evaluation was run.
- The 1200 local task-name records are not the official over-800-task benchmark size reported in the paper framing.
- The representative additions are bounded and are used only to cover task types missing from structured metadata.

## Possible Future Directions

- Memory-conditioned action-space selection.
- Task-stage-aware action cost for GRPO.
- Failure-trace-conditioned replanning.
- Visual-grounding-aware low-level switching.
- World-model-assisted action rollout analysis.