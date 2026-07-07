# MineStudio Module Inventory

This inventory was collected from the clean `minestudio-smoke` environment after a no-deps editable install.

## Top-Level Modules

```text
benchmark
data
inference
models
offline
online
simulator
tutorials
utils
```

## Key Import Checks

| Module | Result | Error / note |
| --- | --- | --- |
| `minestudio` | OK | top-level import passed |
| `minestudio.simulator` | failed | missing `cv2` |
| `minestudio.data` | failed | missing `lmdb` |
| `minestudio.offline` | failed | missing `torch` |
| `minestudio.online` | OK | import passed in this no-deps env |
| `minestudio.inference` | failed | missing `ray` |
| `minestudio.benchmark` | failed | missing `yaml` |
| `minestudio.models` | failed | missing `numpy` |
| `minestudio.utils` | failed | missing `absl` |
| `minestudio.train` | failed | module not present |

## Entry Points And Configs

No MineStudio console entry point was found through package metadata in this no-deps editable install.

Safe config-related paths observed:

```text
.github/workflows/deploy_docs_to_rtd.yml
docs/source/online/config.md
minestudio/benchmark/task_configs
minestudio/online/run/config
tests/test_task_configs.py
```

## Interpretation

The package namespace and source layout are visible, but most practical workflows require dependencies that were intentionally not installed in this bounded pass. This supports using MineStudio as a future engineering base, but not claiming simulator or benchmark execution yet.
