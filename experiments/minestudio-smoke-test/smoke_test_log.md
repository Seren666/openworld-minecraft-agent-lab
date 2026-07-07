# MineStudio Smoke-Test Log

## T0: Install / Import

Status: passed for top-level package import.

Commands:

```bash
python -m pip install --no-deps -e /root/autodl-tmp/external_repos/MineStudio
python - <<'PY'
import importlib, importlib.metadata as md
m = importlib.import_module("minestudio")
print("import minestudio: OK")
print(md.version("minestudio"))
PY
python -m pip show minestudio
```

Key output:

```text
Successfully built minestudio
Successfully installed minestudio-1.1.5
import minestudio: OK
metadata version: 1.1.5
Editable project location: /root/autodl-tmp/external_repos/MineStudio
```

## T1: Module Inventory / Dry Run

Initial status: partial.

Commands:

```bash
python - <<'PY'
import minestudio, pkgutil
print(sorted([m.name for m in pkgutil.iter_modules(minestudio.__path__)]))
PY
```

Key output:

```text
top_level_modules: benchmark, data, inference, models, offline, online, simulator, tutorials, utils
```

Key import checks:

```text
minestudio.simulator: FAILED: ModuleNotFoundError: No module named 'cv2'
minestudio.data: FAILED: ModuleNotFoundError: No module named 'lmdb'
minestudio.offline: FAILED: ModuleNotFoundError: No module named 'torch'
minestudio.online: OK
minestudio.inference: FAILED: ModuleNotFoundError: No module named 'ray'
minestudio.benchmark: FAILED: ModuleNotFoundError: No module named 'yaml'
minestudio.models: FAILED: ModuleNotFoundError: No module named 'numpy'
minestudio.utils: FAILED: ModuleNotFoundError: No module named 'absl'
```

PyTorch check:

```text
torch import: FAILED: ModuleNotFoundError: No module named 'torch'
```

## Blocker-Reduction Pass

Status: partial improvement.

The pass installed only small import-level dependencies and OpenJDK in the existing `/root/autodl-tmp/conda_envs/minestudio-smoke` environment. It did not install PyTorch, Ray, datasets, checkpoints, model weights, Minecraft assets, or raw video tooling.

Commands:

```bash
python -m pip install opencv-python-headless PyYAML absl-py lmdb coloredlogs rich requests lxml
conda install -y -p /root/autodl-tmp/conda_envs/minestudio-smoke openjdk=8
```

Key dependency results:

```text
cv2: OK 5.0.0
numpy: OK 2.2.6
yaml: OK 6.0.3
absl: OK 2.5.0
lmdb: OK 2.2.1
OpenJDK: 1.8.0_152-release
```

T1 import checks after blocker reduction:

```text
minestudio: OK
minestudio.simulator: FAILED: ModuleNotFoundError: No module named 'torch'
minestudio.simulator.MinecraftSim: FAILED: ModuleNotFoundError: No module named 'torch'
minestudio.simulator.entry: FAILED: ModuleNotFoundError: No module named 'torch'
minestudio.benchmark: FAILED: ModuleNotFoundError: No module named 'huggingface_hub'
minestudio.data: FAILED: ModuleNotFoundError: No module named 'torch'
minestudio.models: FAILED: ModuleNotFoundError: No module named 'torch'
minestudio.utils: OK
minestudio.online: OK
minestudio.offline: FAILED: ModuleNotFoundError: No module named 'torch'
minestudio.inference: FAILED: ModuleNotFoundError: No module named 'ray'
```

## T2: Minimal Simulator / Rollout Attempt

Initial status: blocked before rollout.

Command:

```bash
python - <<'PY'
import importlib, shutil, os
print("DISPLAY:", os.environ.get("DISPLAY", "not_set"))
print("Xvfb:", shutil.which("Xvfb"))
print("java:", shutil.which("java"))
for name in ["minestudio.simulator", "minestudio.simulator.MinecraftSim", "minestudio.simulator.entry"]:
    try:
        importlib.import_module(name)
        print(name + ": IMPORT_OK")
    except Exception as exc:
        print(name + ": IMPORT_FAILED: " + type(exc).__name__ + ": " + str(exc).splitlines()[0])
PY
```

Key output:

```text
DISPLAY: not_set
Xvfb: None
java: None
minestudio.simulator: IMPORT_FAILED: ModuleNotFoundError: No module named 'cv2'
minestudio.simulator.MinecraftSim: IMPORT_FAILED: ModuleNotFoundError: No module named 'cv2'
minestudio.simulator.entry: IMPORT_FAILED: ModuleNotFoundError: No module named 'cv2'
```

No simulator reset, no action step, and no rollout was run.

## T2 After Blocker Reduction

Status: blocked before reset or step.

Runtime probe with the environment `bin` directory on `PATH`:

```text
java: /root/autodl-tmp/conda_envs/minestudio-smoke/bin/java
OpenJDK: 1.8.0_152-release
Xvfb: None
DISPLAY: not_set
minestudio.simulator: FAILED: ModuleNotFoundError: No module named 'torch'
```

The immediate `cv2` blocker was resolved, and Java is now available inside the Conda environment. The next simulator import blocker is `torch`. Because PyTorch is a heavy dependency and display support is still missing, no simulator construction, reset, step, rollout, training, checkpoint inference, asset download, or video generation was attempted.
