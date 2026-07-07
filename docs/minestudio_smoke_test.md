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
| PyTorch | not installed in this no-deps smoke env |
| Java | unavailable |
| Display / Xvfb | unavailable |
| Storage note | root filesystem was nearly full; env/cache/temp files were kept under `/root/autodl-tmp` |

`CUDA_VISIBLE_DEVICES=0` was set for the smoke test, although no CUDA workload was run because PyTorch was not installed in this minimal environment.

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
| T1 | module inventory and dry-run checks | list top-level modules; import key modules; inspect config paths | partial | module inventory succeeded; most key modules failed on missing dependencies |
| T2 | minimal simulator / rollout attempt | check display/Java; try simulator imports before launch | blocked | simulator import failed on missing `cv2`; Java, display, and Xvfb were unavailable |

## What Ran Successfully

- AutoDL project repository synced cleanly.
- MineStudio external repository was already present and up to date.
- A clean Python 3.10 environment was created under `/root/autodl-tmp`.
- MineStudio installed in editable no-deps mode.
- `import minestudio` succeeded.
- Package metadata reported version `1.1.5`.
- Top-level module inventory found `benchmark`, `data`, `inference`, `models`, `offline`, `online`, `simulator`, `tutorials`, and `utils`.
- `minestudio.online` imported in the no-deps environment.

## Blockers

- `minestudio.simulator` failed because `cv2` was missing.
- `minestudio.data` failed because `lmdb` was missing.
- `minestudio.offline` failed because `torch` was missing.
- `minestudio.inference` failed because `ray` was missing.
- `minestudio.benchmark` failed because `yaml` was missing.
- `minestudio.models` failed because `numpy` was missing.
- `minestudio.utils` failed because `absl` was missing.
- Java was unavailable in the smoke env.
- `DISPLAY` was unset and `Xvfb` was unavailable.

## Implications For Future Work

This smoke test confirms that MineStudio can be wired into a clean AutoDL environment at the package level without placing environments or caches on the small root filesystem. The next useful step is not a long rollout. It is a bounded dependency pass that installs only enough packages to import the simulator, benchmark, data, and model modules.

Once imports are stable, the next simulator attempt should add Java and display support, then try only a minimal reset and 1-5 scripted/no-op steps.

## Limitations

- This is not an official MineStudio benchmark.
- No model training was run.
- No checkpoint inference was run.
- No Minecraft simulator rollout was run.
- No datasets, checkpoints, model weights, raw videos, or large logs were downloaded or committed.
