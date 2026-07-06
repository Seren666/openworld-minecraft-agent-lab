# MineStudio Second-Pass Install

This note records a bounded second-pass MineStudio setup attempt on the AutoDL machine. It is not a full MineStudio reproduction, training run, or benchmark run.

## Scope

| Item | Value |
| --- | --- |
| External repository | `/root/autodl-tmp/external_repos/MineStudio` |
| Upstream URL | `https://github.com/CraftJarvis/MineStudio.git` |
| Branch | `master` |
| Commit | `278aa8553668d591339dbf30d281594ed06ee882` |
| Conda environment | `minestudio-test` |
| Python | `3.10.20` |
| Package version | `1.1.5` |
| GPU policy | `CUDA_VISIBLE_DEVICES=0` |

## Environment Observations

- The conda environment contains `openjdk 8.0.472`, but `java` was not visible from the non-activated shell PATH during this pass.
- The root filesystem had limited free space after the failed CUDA 12.8 PyTorch install attempt.
- No datasets, checkpoints, videos, or training outputs were downloaded.

## Dependency List Observed

The MineStudio `pyproject.toml` includes heavy and simulator-facing dependencies such as:

```text
av==13.1.0
opencv-python==4.8.0.74
opencv-python-headless==4.8.0.74
gym / gym3 / gymnasium
torch>=2.3.1
lightning
transformers
pyrender
pyglet
ray
minecraft_data==3.20.0
x_transformers==0.27.1
```

## Second-Pass Commands

```bash
export CUDA_VISIBLE_DEVICES=0
source /root/miniconda3/etc/profile.d/conda.sh
cd /root/autodl-tmp/external_repos/MineStudio
conda run -n minestudio-test python --version
conda list -n minestudio-test openjdk
timeout 300s conda run -n minestudio-test python -m pip install --dry-run --report /root/autodl-tmp/logs/minestudio_second_pass_dry_run_report.json -e .
timeout 120s conda run -n minestudio-test python -m pip install --no-deps -e .
```

## Results

| Check | Result |
| --- | --- |
| Python version | Passed, `Python 3.10.20` |
| `openjdk` package | Present in conda env: `8.0.472` |
| Shell `java -version` | Failed from current non-activated PATH |
| Full/dry-run dependency resolution | Timed out after 300 seconds with no useful log output |
| No-deps editable install | Passed |
| Top-level `import minestudio` | Passed |
| `import torch` | Failed, `ModuleNotFoundError: No module named 'torch'` |
| `import cv2` | Failed, `ModuleNotFoundError: No module named 'cv2'` |
| `import minestudio.simulator` | Failed because `cv2` is missing |

## Interpretation

The second pass confirms the earlier smoke-test result: the source package itself can be installed and imported, but the usable simulator stack remains blocked by dependency installation. The immediate blocker is not a Minecraft task or model asset; it is environment stabilization.

Given the disk-space pressure, Blackwell/PyTorch compatibility issue, missing OpenCV, and simulator/rendering dependencies, MineStudio should be deferred until the dependency strategy is stable. It remains a good future engineering base for benchmark evaluation and failure case analysis, but it is not the fastest path to additional evidence today.

## Next Step

For a future pass:

1. Free or expand root filesystem space before installing PyTorch/CUDA wheels.
2. Activate `minestudio-test` normally and verify `java -version` from inside the environment.
3. Install dependencies in small groups: OpenCV first, PyTorch second, simulator/rendering packages third.
4. Only after imports pass, try the smallest documented simulator example under a short timeout.
