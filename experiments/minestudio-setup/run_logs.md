# MineStudio Run Logs

Keep compact Markdown summaries of setup and demo runs here. Large raw logs should stay out of Git.

## 2026-07-06 Smoke Test

### Goal

Check whether MineStudio can be installed and minimally used on the AutoDL machine without downloading large datasets, checkpoints, or starting training jobs.

### Raw Log Location

Raw logs were kept outside the repository:

```text
/root/autodl-tmp/logs/minestudio_smoke_2026-07-06.log
/root/autodl-tmp/logs/minestudio_smoke_nodeps_2026-07-06.log
```

These files were not committed.

### Repository Inspection

| Item | Result |
| --- | --- |
| Official repository | `https://github.com/CraftJarvis/MineStudio.git` |
| Branch | `master` |
| Commit | `278aa8553668d591339dbf30d281594ed06ee882` |
| Version | `1.1.5` |
| External clone path | `/root/autodl-tmp/external_repos/MineStudio` |

### Setup Commands

```bash
export CUDA_VISIBLE_DEVICES=0
source /root/miniconda3/etc/profile.d/conda.sh
conda create -y -n minestudio-test -c conda-forge python=3.10 openjdk=8
conda run -n minestudio-test python --version
conda run -n minestudio-test java -version
timeout 900s conda run -n minestudio-test python -m pip install -q minestudio
```

### Results

| Check | Result |
| --- | --- |
| Conda env creation | Passed |
| Python version | `Python 3.10.20` |
| Java version | `OpenJDK 1.8.0_472` |
| Full `pip install minestudio` | Failed by timeout after 900 seconds, exit code `124` |
| `pip show minestudio` after full install | Failed because package was not installed |
| Top-level import after full install | Failed because package was not installed |
| Simulator entry | Failed because package was not installed |

### No-Deps Source Packaging Check

```bash
conda run -n minestudio-test python -m pip install --no-deps -e /root/autodl-tmp/external_repos/MineStudio
conda run -n minestudio-test python -m pip show minestudio
conda run -n minestudio-test python -c 'import minestudio; print("minestudio namespace import ok")'
conda run -n minestudio-test python -c 'import torch; print(torch.__version__, torch.cuda.is_available())'
conda run -n minestudio-test python -c 'from minestudio.simulator import MinecraftSim; print("MinecraftSim import ok")'
```

| Check | Result |
| --- | --- |
| Editable no-deps install | Passed |
| `pip show minestudio` | Passed, version `1.1.5` |
| Top-level `import minestudio` | Passed |
| PyTorch GPU check | Failed: `ModuleNotFoundError: No module named 'torch'` |
| `MinecraftSim` import | Failed: `ModuleNotFoundError: No module named 'cv2'` |

### Interpretation

The repository and package metadata look promising, but the full environment was not ready after a bounded smoke test. MineStudio remains relevant for future benchmark evaluation and failure case analysis, but the next pass should focus on dependency installation and rendering setup rather than model training or dataset download.

### Next Step

Run a dependency-focused pass with a longer but still bounded install window, then test imports in this order:

1. `import torch`
2. `import cv2`
3. `import minestudio`
4. `from minestudio.simulator import MinecraftSim`
5. `timeout 60s python -m minestudio.simulator.entry`
