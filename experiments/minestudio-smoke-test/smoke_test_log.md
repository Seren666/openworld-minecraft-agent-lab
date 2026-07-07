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

Status: partial.

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

## T2: Minimal Simulator / Rollout Attempt

Status: blocked before rollout.

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
