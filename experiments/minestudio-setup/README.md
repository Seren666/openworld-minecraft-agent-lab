# MineStudio Setup Smoke Test

This folder records a bounded MineStudio setup smoke test on the AutoDL machine. It is not a full MineStudio reproduction, training run, or benchmark run.

## Why MineStudio Matters

MineStudio is a CraftJarvis toolkit for Minecraft agent research. It matters for this project because it connects several engineering pieces that later papers and experiments need:

- Minecraft simulator access
- Trajectory data loading
- Policy model templates
- Offline and online training pipelines
- Inference utilities
- Benchmark and failure-analysis workflows

For an advisor email, the useful evidence is not a long training run. The useful evidence is whether the toolkit can be installed, imported, and used as a plausible engineering base for later Minecraft agent experiments.

## Upstream Repository

| Item | Value |
| --- | --- |
| Repository | `https://github.com/CraftJarvis/MineStudio.git` |
| Branch | `master` |
| Commit | `278aa8553668d591339dbf30d281594ed06ee882` |
| Version in `pyproject.toml` | `1.1.5` |
| AutoDL external path | `/root/autodl-tmp/external_repos/MineStudio` |

External source code stays under `/root/autodl-tmp/external_repos` and is not committed to this repository.

## Setup Result

| Check | Result |
| --- | --- |
| Clone official repository | Passed |
| Create separate Conda environment `minestudio-test` | Passed |
| Python version | Python 3.10.20 |
| Java requirement | OpenJDK 8 installed in the environment |
| Full `pip install minestudio` | Timed out after 15 minutes |
| Second-pass dependency dry-run | Timed out after 5 minutes |
| No-deps editable install from source | Passed |
| Top-level `import minestudio` | Passed after no-deps editable install |
| PyTorch GPU check | Not available because full dependency installation timed out before `torch` was installed |
| `MinecraftSim` import | Failed after no-deps install because dependencies such as `cv2` were missing |
| Simulator launch | Not run successfully; full simulator requires dependencies and rendering tools |

## What Worked

- The official repository cloned successfully on AutoDL.
- The repository metadata, README, and `pyproject.toml` were inspected.
- A clean Conda environment was created without modifying the base environment aggressively.
- Python 3.10 and OpenJDK 8 were available inside the environment.
- The package namespace could be installed from source with `--no-deps` and imported.

## What Failed Or Remains Unresolved

- Full dependency installation did not complete within the 15-minute bound.
- A second-pass dependency dry-run also timed out within the 5-minute bound.
- `torch` was not installed, so CUDA availability through PyTorch could not be tested in this environment.
- `MinecraftSim` import failed because `cv2` and other dependencies were not installed.
- `java` was present as a conda `openjdk` package but was not visible from the non-activated shell PATH during the second pass.
- The simulator also requires rendering setup such as Xvfb or VirtualGL.
- No datasets, checkpoints, or simulator assets were downloaded.

## Suitability As Future Engineering Base

MineStudio looks suitable as a future engineering base, but only after dependency installation is stabilized. It is especially relevant for benchmark evaluation and failure case analysis because it provides simulator, model, inference, and benchmark modules in one toolkit.

For the next pass, the priority should be dependency installation strategy rather than training:

- Try a longer but bounded install window.
- Consider installing from source with dependencies in smaller groups.
- Install rendering support with Xvfb or VirtualGL.
- Run the smallest simulator example only after import and PyTorch checks pass.

## Files

- `install_notes.md`: exact setup commands and dependency notes
- `second_pass_install.md`: bounded second-pass dependency attempt
- `run_logs.md`: summarized smoke-test results
- `screenshots/`: small setup screenshots if needed later
