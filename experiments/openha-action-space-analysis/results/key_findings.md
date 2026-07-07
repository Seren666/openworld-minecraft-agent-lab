# Key Findings

This is a preliminary rule-based taxonomy over OpenHA/CrossAgent public task metadata and a bounded representative sample. It is not official model evaluation.

## Strongest Findings

1. **1200 tasks were analyzed.** The task set is dominated by metadata-derived Minecraft tasks from public OpenHA/CrossAgent files, with a small representative supplement for missing task types.
2. **crafting accounts for 238 tasks (19.8%).** This category needs different interface support than a single fixed action space.
3. **dynamic_action_space_switching is assigned to 463 tasks (38.6%).** This supports treating action-space choice as task- and stage-dependent.
4. **Memory/prerequisite reasoning appears in 851 tasks (70.9%).** Crafting, smelting, mining with tool constraints, and long-horizon obtain tasks are especially sensitive to missing prerequisites.
5. **Visual grounding appears in 737 tasks (61.4%).** Mining, combat, furnace use, navigation, and building tasks require target localization beyond text-only planning.

## Cautious Hypotheses

- Long-horizon obtain tasks may benefit from memory-conditioned action-space selection.
- Crafting and smelting tasks appear more dependent on prerequisite and inventory state than on raw low-level control alone.
- Mining, combat, navigation, and building tasks appear more dependent on visual grounding and low-level control than recipe-only tasks.

## Limitations

- The taxonomy is rule-based and preliminary.
- Task names and public metadata may not reveal full trajectory difficulty.
- No official OpenHA/CrossAgent checkpoint inference or Minecraft evaluation was run.
- The representative additions are bounded and are used only to cover task types missing from structured metadata.

## Possible Future Directions

- Memory-conditioned action-space selection.
- Task-stage-aware action cost for GRPO.
- Failure-trace-conditioned replanning.
- Visual-grounding-aware low-level switching.
- World-model-assisted action rollout analysis.