# MineStudio Smoke-Test Setup Log

This is a sanitized command log from the bounded AutoDL smoke test. It omits private access details and does not include external repository source code.

## Storage And System Check

```bash
df -h / /root/autodl-tmp
free -h
```

Key output:

```text
/ had about 2.0G free and was about 94% used.
/root/autodl-tmp had about 539G free and was about 3% used.
System RAM was about 1.0TiB total.
```

```bash
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader
nvcc --version
```

Key output:

```text
6 x NVIDIA RTX PRO 6000 Blackwell Server Edition
97887 MiB per GPU
Driver 595.71.05
CUDA compiler release 11.8
```

```bash
python --version
conda --version
git --version
java -version
```

Key output:

```text
Python 3.10.8
conda 22.11.1
git version 2.34.1
java: command not found
```

## Project Repository Sync

```bash
cd /root/autodl-tmp/openworld-minecraft-agent-lab
git status --short --branch
git pull --rebase
git status --short --branch
```

Key output:

```text
Before sync: ## main...origin/main
Pull result: fast-forwarded to the latest origin/main.
After sync: ## main...origin/main
```

## MineStudio Repository

```bash
mkdir -p /root/autodl-tmp/external_repos
cd /root/autodl-tmp/external_repos/MineStudio
git status --short --branch
git pull --rebase || true
git remote -v
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD
```

Key output:

```text
Branch: master
Commit: 278aa8553668d591339dbf30d281594ed06ee882
Update result: Already up to date.
```

```bash
find . -maxdepth 2 -mindepth 1 | sort | head -120
ls -1 pyproject.toml setup.py setup.cfg requirements*.txt environment*.yml environment*.yaml docs README* 2>/dev/null
grep -nE 'python_requires|requires-python|python =' pyproject.toml setup.py setup.cfg 2>/dev/null
```

Key output:

```text
Top-level project content included assets, docs, minestudio, tests, README.md, and pyproject.toml.
Dependency file found: pyproject.toml
Documentation dependency file found: docs/requirements.txt
Python requirement: requires-python = ">=3.10"
```

## Conda Environment

```bash
mkdir -p /root/autodl-tmp/conda_envs /root/autodl-tmp/pip_cache /root/autodl-tmp/tmp
conda create -y -p /root/autodl-tmp/conda_envs/minestudio-smoke python=3.10 pip
/root/autodl-tmp/conda_envs/minestudio-smoke/bin/python --version
/root/autodl-tmp/conda_envs/minestudio-smoke/bin/python -m pip --version
```

Key output:

```text
Environment location: /root/autodl-tmp/conda_envs/minestudio-smoke
Python 3.10.20
pip 26.1.2
Environment size after smoke test: about 197M
```

## T0 Install / Import

```bash
cd /root/autodl-tmp/external_repos/MineStudio
/root/autodl-tmp/conda_envs/minestudio-smoke/bin/python -m pip install --no-deps -e .
/root/autodl-tmp/conda_envs/minestudio-smoke/bin/python -m pip show minestudio
```

Key output:

```text
Successfully built minestudio
Successfully installed minestudio-1.1.5
Package summary: A simple and efficient Minecraft Agent development kit for AI research.
Editable project location: /root/autodl-tmp/external_repos/MineStudio
```

```bash
/root/autodl-tmp/conda_envs/minestudio-smoke/bin/python - <<'PY'
import importlib, importlib.metadata as md
m = importlib.import_module("minestudio")
print("import minestudio: OK")
print(md.version("minestudio"))
PY
```

Key output:

```text
import minestudio: OK
metadata version: 1.1.5
```

## T1 Module Inventory

```bash
/root/autodl-tmp/conda_envs/minestudio-smoke/bin/python - <<'PY'
import minestudio, pkgutil
print(sorted([m.name for m in pkgutil.iter_modules(minestudio.__path__)]))
PY
```

Key output:

```text
benchmark, data, inference, models, offline, online, simulator, tutorials, utils
```

```bash
/root/autodl-tmp/conda_envs/minestudio-smoke/bin/python - <<'PY'
import importlib
for name in [
    "minestudio.simulator",
    "minestudio.data",
    "minestudio.offline",
    "minestudio.online",
    "minestudio.inference",
    "minestudio.benchmark",
    "minestudio.models",
    "minestudio.utils",
]:
    try:
        importlib.import_module(name)
        print(name + ": OK")
    except Exception as exc:
        print(name + ": FAILED: " + type(exc).__name__ + ": " + str(exc).splitlines()[0])
PY
```

Key output:

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

## T2 Simulator Readiness

```bash
/root/autodl-tmp/conda_envs/minestudio-smoke/bin/python - <<'PY'
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

No simulator reset, action step, rollout, training, dataset download, checkpoint download, or raw video generation was run.
