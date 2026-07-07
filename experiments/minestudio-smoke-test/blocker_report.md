# MineStudio Smoke-Test Blocker Report

## Summary

The minimal MineStudio workflow reached top-level install/import, but simulator and most workflow modules remain blocked by missing dependencies and system/runtime requirements.

## Blockers

| Area | Evidence | Impact |
| --- | --- | --- |
| Full dependency stack | no-deps install was used; key imports failed on missing packages | T1 is partial; real data, model, benchmark, and simulator workflows need dependency installation |
| Simulator import | `minestudio.simulator` failed on missing `cv2` | T2 could not reach environment initialization |
| PyTorch | `torch` import failed | offline training, model modules, and CUDA checks through PyTorch cannot run in this env |
| Data pipeline | `minestudio.data` failed on missing `lmdb` | dataset workflows are unavailable in this env |
| Inference / distributed tooling | `minestudio.inference` failed on missing `ray` | inference workflow cannot be tested yet |
| Benchmark module | `minestudio.benchmark` failed on missing `yaml` | benchmark configs cannot be loaded yet |
| Rendering/system tools | `DISPLAY` unset, `Xvfb` unavailable, Java unavailable | simulator launch is not ready |

## What Not To Claim

- Do not claim MineStudio simulator execution.
- Do not claim Minecraft rollout success.
- Do not claim official MineStudio benchmark evaluation.
- Do not claim checkpoint inference or model training.

## Recommended Next Pass

1. Install a bounded dependency subset for imports only: `numpy`, `PyYAML`, `absl-py`, `opencv-python-headless`, `lmdb`.
2. Install a Blackwell-compatible PyTorch build under `/root/autodl-tmp`.
3. Add Java and display support only after import checks pass.
4. Attempt simulator initialization only after `minestudio.simulator` imports cleanly.
5. Keep any simulator output text-only unless a tiny screenshot is explicitly useful and under repository size limits.
