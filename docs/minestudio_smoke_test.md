# MineStudio Minimal Workflow Smoke Test

## Motivation

MineStudio matters for Minecraft open-world agent experiments because it provides the engineering layer around simulator access, data loading, training workflows, inference utilities, benchmarks, and wrappers. For this repository, the immediate goal is not official evaluation. The goal is to identify which parts of the workflow can run cleanly on AutoDL and which dependencies still block simulator work.

## Environment

| Item | Result |
| --- | --- |
| GPU | `6 x NVIDIA RTX PRO 6000 Blackwell Server Edition` |
| GPU memory | about `97,887 MiB` each |
| Driver | `595.71.05` |
| CUDA compiler | `11.8` |
| Conda env | `/root/autodl-tmp/conda_envs/minestudio-smoke` |
| Python | `3.10.20` |
| PyTorch | not installed in this bounded import-level env |
| Java | OpenJDK 8 available inside the Conda env after blocker-reduction pass |
| Display / Xvfb | unavailable |
| Storage note | root filesystem was nearly full; env/cache/temp files were kept under `/root/autodl-tmp` |

`CUDA_VISIBLE_DEVICES=0` was set for the smoke test, although no CUDA workload was run because PyTorch was not installed in this bounded environment.

## External Repo

| Item | Value |
| --- | --- |
| Repository | `https://github.com/CraftJarvis/MineStudio.git` |
| Branch | `master` |
| Commit | `278aa8553668d591339dbf30d281594ed06ee882` |
| Version | `1.1.5` |
| Python requirement | `>=3.10` |

The external repository remained under `/root/autodl-tmp/external_repos/MineStudio` and was not copied into this project.

## Test Tiers

| Tier | Goal | Command summary | Status | Result / blocker |
| --- | --- | --- | --- | --- |
| T0 | install/import smoke test | create Python 3.10 env; `pip install --no-deps -e .`; import `minestudio`; inspect package metadata | passed | top-level import succeeded; package metadata reports `1.1.5` |
| T1 | module inventory and dry-run checks | install small import dependencies; list top-level modules; import key modules | partial, improved | `cv2`, `numpy`, `yaml`, `absl`, `lmdb`, `minestudio.utils`, and `minestudio.online` now import; simulator/data/model/offline paths now stop at missing `torch` |
| T2 | minimal simulator / runtime probe | check Java/display; try simulator import before reset | blocked | simulator import now fails on missing `torch`; Java is available in the env, but `DISPLAY` and Xvfb are still unavailable |

## What Ran Successfully

- AutoDL project repository synced cleanly.
- MineStudio external repository was already present and up to date.
- A clean Python 3.10 environment was created under `/root/autodl-tmp`.
- MineStudio installed in editable no-deps mode.
- `import minestudio` succeeded.
- Package metadata reported version `1.1.5`.
- Top-level module inventory found `benchmark`, `data`, `inference`, `models`, `offline`, `online`, `simulator`, `tutorials`, and `utils`.
- `minestudio.online` imported in the no-deps environment.
- The immediate `cv2` blocker was resolved by installing `opencv-python-headless`.
- Small import dependencies `numpy`, `PyYAML`, `absl-py`, `lmdb`, `coloredlogs`, `rich`, `requests`, and `lxml` were installed.
- `minestudio.utils` now imports.
- OpenJDK 8 is available inside the `minestudio-smoke` Conda environment when the env `bin` directory is on `PATH`.

## Blockers

- `minestudio.simulator` now fails because `torch` is missing.
- `minestudio.data`, `minestudio.models`, and `minestudio.offline` also stop at missing `torch`.
- `minestudio.benchmark` progressed past `yaml` and now stops at missing `huggingface_hub`.
- `minestudio.inference` still fails because `ray` is missing.
- `DISPLAY` was unset and `Xvfb` was unavailable.
- The installed `opencv-python-headless` version is sufficient for `cv2` import, but it is newer than the version pinned by MineStudio metadata. A stricter dependency pass should align versions intentionally.

## Implications For Future Work

This smoke test confirms that MineStudio can be wired into a clean AutoDL environment at the package level without placing environments or caches on the small root filesystem. The blocker-reduction pass also confirms that the first simulator import blocker can be moved from `cv2` to `torch` without installing datasets, checkpoints, or model weights.

The next useful step is not a long rollout. It is a bounded dependency pass that installs a Blackwell-compatible PyTorch build and display support, then rechecks simulator import before any reset or step attempt.

## Limitations

- This is not an official MineStudio benchmark.
- No model training was run.
- No checkpoint inference was run.
- No Minecraft simulator rollout was run.
- No datasets, checkpoints, model weights, raw videos, or large logs were downloaded or committed.
