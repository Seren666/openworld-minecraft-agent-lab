# Manual Sanity-Check Protocol

This protocol documents the first-pass sanity check for the OpenHA/CrossAgent action-space taxonomy. It is a qualitative check, not an official validation result.

## Sample

- File: `manual_check_sample_100.csv`
- Size: 100 task records
- Sampling: deterministic stratified sample across predicted categories, with rare categories retained when available.
- Source: `task_taxonomy.csv`

## Labeling Rules

- `manual_category` uses conservative task-name interpretation. When task prefixes such as `craft_item`, `mine_block`, `smelt_item`, `kill_entity`, `interact_block`, or `drop:` are present, the prefix is prioritized over item semantics.
- `manual_interfaces` lists the action interfaces that appear necessary from the task name alone.
- `confidence` is `high` when the task verb/prefix clearly supports the first-pass label, `medium` when the task name is plausible but missing trajectory context, and `low` when the task name is too ambiguous for reliable labeling.
- `notes` explain whether the first-pass label agrees with the rule prediction or needs trajectory-level review.

## What This Check Does Not Claim

- It does not validate the taxonomy against official OpenHA/CrossAgent labels.
- It does not use simulator rollouts, trajectories, model outputs, or checkpoint inference.
- It does not report agreement as a benchmark metric.
- It does not change the official over-800-task benchmark framing from the papers.

## Next Step

A stronger validation pass would use benchmark task definitions or summarized trajectories and would compute category/interface agreement after independent annotation.
