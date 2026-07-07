# Metadata Source Report

This report documents the source used for the OpenHA/CrossAgent action-space taxonomy analysis.

## Source Location

| Field | Value |
| --- | --- |
| OpenHA repository URL | https://github.com/CraftJarvis/OpenHA |
| Branch | `main` |
| Commit hash | `606efc69e945bd02c700e584136bcc105d22f122` |
| Local source kind | `zip` |
| Local source storage | external repository or snapshot inspected outside this project repository |
| Analysis scope | full local metadata-derived task names plus bounded representative additions |

## Directory Structure Summary

- Root README and package metadata are available in the OpenHA snapshot.
- `CrossAgent/` is present.
- CrossAgent subfolders observed: `MTRL, SFT, STRL, examples`.
- Minecraft-related task family files observed: `openagents/envs/tasks/__init__.py, openagents/envs/tasks/craft_item.py, openagents/envs/tasks/interact_block.py, openagents/envs/tasks/kill_entity.py, openagents/envs/tasks/mine_block.py, openagents/envs/tasks/smelt_item.py, openagents/envs/tasks/task_manager.py`.
- `openagents/assets/recipes/` is present in the snapshot, but raw recipe files are not copied into this repository.

## Task Metadata Found

| Source | Count |
| --- | ---: |
| `CrossAgent/STRL/data_processor/utils/task_list.json` tasks | 30 |
| unique task names from `CrossAgent/STRL/data_processor/task_suc_rate.json` | 1192 |
| task names inferred from rollout debug directory names | 9 |
| task rows analyzed after de-duplication and representative additions | 1200 |

## Metadata Type

The strongest local source is structured JSON task metadata from the public OpenHA/CrossAgent repository snapshot. The taxonomy uses task names and public summary metadata only. It does not copy raw external repository code, raw rollout logs, model weights, datasets, checkpoints, or videos into this project repository.

## Limitations

- Task names do not fully reveal trajectory difficulty, visual state, inventory state, or world layout.
- `task_suc_rate.json` appears to be public aggregate task-level metadata, not an official evaluation run performed in this repository.
- The taxonomy is rule-based and preliminary.
- Representative tasks are added only to cover shelter, cave exploration, furnace use, and other task types not visible in the structured task-name list.
