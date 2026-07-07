# Metadata Source Report

This report documents the source used for the OpenHA/CrossAgent action-space taxonomy analysis.

This is not the official OpenHA benchmark size. The OpenHA/CrossAgent papers describe the benchmark scope as over 800 distinct Minecraft tasks. This local artifact contains task-name records parsed from public metadata/config files plus bounded representative additions.

## Source Location

| Field | Value |
| --- | --- |
| OpenHA repository URL | https://github.com/CraftJarvis/OpenHA |
| Branch | `main` |
| Commit hash | `606efc69e945bd02c700e584136bcc105d22f122` |
| Local source kind | `zip` |
| Local source storage | external repository or snapshot inspected outside this project repository |
| Analysis scope | exploratory metadata/config-derived task-name records plus bounded representative additions |

## Directory Structure Summary

- Root README and package metadata are available in the OpenHA snapshot.
- `CrossAgent/` is present.
- CrossAgent subfolders observed: `MTRL, SFT, STRL, examples`.
- Minecraft-related task family files observed: `openagents/envs/tasks/__init__.py, openagents/envs/tasks/craft_item.py, openagents/envs/tasks/interact_block.py, openagents/envs/tasks/kill_entity.py, openagents/envs/tasks/mine_block.py, openagents/envs/tasks/smelt_item.py, openagents/envs/tasks/task_manager.py`.
- `openagents/assets/recipes/` is present in the snapshot, but raw recipe files are not copied into this repository.

## Source Breakdown

| Source path | Source type | Raw unique names found | Final rows mentioning source | Exclusive new rows after exact-name de-duplication | Entry interpretation |
| --- | --- | ---: | ---: | ---: | --- |
| `CrossAgent/STRL/data_processor/task_suc_rate.json` | CrossAgent metadata/config summary | 1192 | 1192 | 1162 | task-name records / atomic or config-level task variants, not the official benchmark-size denominator |
| `CrossAgent/STRL/data_processor/utils/task_list.json` | CrossAgent task-list/config file | 30 | 30 | 0 | task-list entries that overlap with `task_suc_rate.json` in this snapshot |
| rollout-debug directory names | generated/debug directory labels | 9 | 9 | 0 | directory-derived task labels that overlap with config metadata; not new benchmark tasks |
| `manual_representative_sample` | manually added analysis sample | 8 | 8 | 8 | bounded Minecraft examples added only to cover readable task types such as shelter, cave exploration, and furnace use |

## Final Row-Source Combinations

| Final `source` value in `task_taxonomy.csv` | Row count |
| --- | ---: |
| `CrossAgent/STRL/data_processor/task_suc_rate.json` | 1162 |
| `CrossAgent/STRL/data_processor/utils/task_list.json; CrossAgent/STRL/data_processor/task_suc_rate.json` | 21 |
| `CrossAgent/STRL/data_processor/utils/task_list.json; CrossAgent/STRL/data_processor/task_suc_rate.json; rollout_debug directory names` | 9 |
| `manual_representative_sample` | 8 |

## Final CSV Accounting

| Statistic | Count |
| --- | ---: |
| Rows in `task_taxonomy.csv` | 1200 |
| Unique task names in `task_taxonomy.csv` | 1200 |
| Duplicate exact task names in final CSV | 0 |

The final CSV de-duplicates exact task names. Upstream sources overlap conceptually and by exact name, so source counts should not be added together as an official benchmark count.

## Metadata Type

The strongest local source is structured JSON task metadata from the public OpenHA/CrossAgent repository snapshot. The taxonomy uses task names and public summary/config metadata only. It does not copy raw external repository code, raw rollout logs, model weights, datasets, checkpoints, or videos into this project repository.

## Limitations

- Task names do not fully reveal trajectory difficulty, visual state, inventory state, or world layout.
- `task_suc_rate.json` appears to be public aggregate task-level metadata/config output, not an official evaluation run performed in this repository.
- The 1200 local records are not the official OpenHA/CrossAgent benchmark size.
- The taxonomy is rule-based and preliminary.
- Representative tasks are added only to cover shelter, cave exploration, furnace use, and other task types not visible in the structured task-name list.
