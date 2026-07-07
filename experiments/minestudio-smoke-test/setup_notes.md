# MineStudio Smoke-Test Setup Notes

## Scope

This was a minimal workflow smoke test, not a full dependency installation or official benchmark run. The test avoided large datasets, model weights, checkpoints, raw videos, and long-running jobs.

## Storage Decisions

- External repository: `/root/autodl-tmp/external_repos/MineStudio`
- Conda env: `/root/autodl-tmp/conda_envs/minestudio-smoke`
- Pip cache: `/root/autodl-tmp/pip_cache`
- Temporary files: `/root/autodl-tmp/tmp`

The root filesystem had about `2.0G` free, while `/root/autodl-tmp` had about `539G` free. Keeping the environment and caches under `/root/autodl-tmp` was necessary.

## Repository Audit

| Item | Result |
| --- | --- |
| Repository URL | `https://github.com/CraftJarvis/MineStudio.git` |
| Branch | `master` |
| Commit | `278aa8553668d591339dbf30d281594ed06ee882` |
| Python requirement | `>=3.10` in `pyproject.toml` |
| Package version | `1.1.5` |

Top-level directories observed:

- `assets`
- `docs`
- `minestudio`
- `tests`

MineStudio package modules observed:

- `benchmark`
- `data`
- `inference`
- `models`
- `offline`
- `online`
- `simulator`
- `tutorials`
- `utils`

## Environment

| Item | Result |
| --- | --- |
| Base Python | `3.10.8` |
| Conda | `22.11.1` |
| Smoke env Python | `3.10.20` |
| Git | `2.34.1` |
| GPU | `6 x NVIDIA RTX PRO 6000 Blackwell Server Edition` |
| GPU memory | about `97,887 MiB` per GPU |
| Driver | `595.71.05` |
| CUDA compiler | `11.8` |
| Java | unavailable |
| Xvfb | unavailable |
| Display | unset |

## Install Strategy

The full dependency stack is large and was already known to be difficult from earlier bounded attempts. For this clean pass, the test used:

```bash
pip install --no-deps -e /root/autodl-tmp/external_repos/MineStudio
```

This verifies package metadata, editable source wiring, and top-level import without pulling the full simulator, training, model, and data stack.
