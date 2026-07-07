# MineStudio Smoke-Test Blocker Report

## Summary

The minimal MineStudio workflow reached top-level install/import. A bounded blocker-reduction pass resolved the immediate `cv2` import blocker and installed OpenJDK 8 inside the data-disk Conda environment, but simulator import still does not reach reset or step.

## Blockers

| Area | Evidence | Impact |
| --- | --- | --- |
| Full dependency stack | only small import-level dependencies were installed | T1 is still partial; real data, model, benchmark, and simulator workflows need more dependencies |
| `cv2` blocker | `opencv-python-headless` installed and `cv2` imports | immediate simulator blocker was reduced |
| Simulator import | `minestudio.simulator` now fails on missing `torch` | T2 still cannot reach environment construction, reset, or step |
| PyTorch | `torch` import failed | simulator, offline training, data/model modules, and CUDA checks through PyTorch cannot run in this env |
| Data pipeline | `minestudio.data` progressed past `lmdb` and now fails on missing `torch` | dataset workflows remain unavailable |
| Inference / distributed tooling | `minestudio.inference` failed on missing `ray` | inference workflow cannot be tested yet |
| Benchmark module | `minestudio.benchmark` progressed past `yaml` and now fails on missing `huggingface_hub` | benchmark configs still cannot be loaded fully |
| Java | OpenJDK 8 installed inside `/root/autodl-tmp/conda_envs/minestudio-smoke` | Java is available when the env `bin` directory is on `PATH` |
| Rendering/system tools | `DISPLAY` unset and `Xvfb` unavailable | simulator launch is not ready |

## What Not To Claim

- Do not claim MineStudio simulator execution.
- Do not claim Minecraft rollout success.
- Do not claim official MineStudio benchmark evaluation.
- Do not claim checkpoint inference or model training.

## Recommended Next Pass

1. Install a Blackwell-compatible PyTorch build under `/root/autodl-tmp`, then re-run only import-level checks.
2. Align OpenCV/Numpy versions with MineStudio metadata if stricter simulator behavior is needed.
3. Add display support such as Xvfb or VirtualGL before any graphical simulator launch.
4. Install small benchmark/import dependencies such as `huggingface_hub` only if benchmark config parsing becomes the next target.
5. Attempt simulator initialization only after `minestudio.simulator` imports cleanly.
6. Keep any simulator output text-only unless a tiny screenshot is explicitly useful and under repository size limits.
