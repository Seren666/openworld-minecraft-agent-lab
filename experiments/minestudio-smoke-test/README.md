# MineStudio Minimal Workflow Smoke Test

This folder records a bounded MineStudio smoke test on the AutoDL machine. It is not an official MineStudio benchmark, training run, checkpoint inference run, or Minecraft evaluation.

## Goal

The goal was to verify the smallest safe part of the MineStudio workflow that can run without downloading datasets, model weights, checkpoints, raw videos, or large logs.

## Upstream Repository

| Item | Value |
| --- | --- |
| Repository | `https://github.com/CraftJarvis/MineStudio.git` |
| Branch | `master` |
| Commit | `278aa8553668d591339dbf30d281594ed06ee882` |
| Version | `1.1.5` |
| External path | `/root/autodl-tmp/external_repos/MineStudio` |

External source code stays outside this repository.

## Environment

| Item | Result |
| --- | --- |
| Conda env | `/root/autodl-tmp/conda_envs/minestudio-smoke` |
| Python | `3.10.20` |
| Env size | about `197M` |
| GPU | `6 x NVIDIA RTX PRO 6000 Blackwell Server Edition`, about `97.9 GiB` each |
| Driver | `595.71.05` |
| CUDA compiler | `11.8` |
| Java | not available in this smoke env |
| Xvfb / display | not available / `DISPLAY` unset |
| PyTorch | not installed in this minimal no-deps pass |

The root filesystem was nearly full, so the environment, cache, temp files, and external repo were kept under `/root/autodl-tmp`.

## Tier Status

| Tier | Goal | Status | Result |
| --- | --- | --- | --- |
| T0 | install/import smoke test | passed | no-deps editable install succeeded; `import minestudio` succeeded; package metadata reports `1.1.5` |
| T1 | module inventory and dry-run checks | partial | top-level package modules were discovered; most key module imports require missing optional dependencies |
| T2 | minimal simulator / rollout attempt | blocked | simulator import failed before launch because `cv2` was missing; Java, display, and Xvfb were also unavailable |

## Strongest Verified Success

The clean environment under `/root/autodl-tmp` can install MineStudio from the external repository with `pip install --no-deps -e .` and import the top-level `minestudio` package.

## Main Blocker

The simulator and most workflow modules require the full MineStudio dependency stack. In the bounded no-deps pass, imports failed on dependencies such as `cv2`, `lmdb`, `torch`, `ray`, `yaml`, `numpy`, and `absl`. A simulator rollout was not attempted because the simulator import itself failed and the environment lacked Java/display support.

## Files

- `logs/setup_log.md`: sanitized command log and key outputs
- `setup_notes.md`: setup decisions and environment details
- `module_inventory.md`: top-level modules and import results
- `smoke_test_log.md`: T0/T1/T2 smoke-test results
- `blocker_report.md`: concrete blockers and next steps
- `resume_bullet.md`: short result summaries
