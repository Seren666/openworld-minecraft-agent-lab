# MineStudio Install Notes

## Environment

| Item | Value |
| --- | --- |
| Machine | AutoDL remote environment |
| Repository path | `/root/autodl-tmp/openworld-minecraft-agent-lab` |
| External source path | `/root/autodl-tmp/external_repos/MineStudio` |
| GPU policy | `CUDA_VISIBLE_DEVICES=0` |
| GPU available on machine | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| Driver / CUDA from earlier audit | Driver `595.71.05`, `nvidia-smi` CUDA `13.2`, `nvcc` CUDA `11.8` |
| Conda env | `minestudio-test` |
| Python | `3.10.20` |
| Java | OpenJDK `1.8.0_472` |

## Upstream Source

```bash
cd /root/autodl-tmp/external_repos
git clone https://github.com/CraftJarvis/MineStudio.git
cd MineStudio
git branch --show-current
git rev-parse HEAD
```

Recorded result:

```text
origin: https://github.com/CraftJarvis/MineStudio.git
branch: master
commit: 278aa8553668d591339dbf30d281594ed06ee882
version: 1.1.5
```

## Official Installation Instructions Observed

The README states:

```bash
conda create -n minestudio python=3.10 -y
conda activate minestudio
conda install --channel=conda-forge openjdk=8 -y
pip install MineStudio
```

It also states that the Minecraft simulator requires rendering tools. NVIDIA users are pointed to VirtualGL, while other users can use Xvfb. The simulator is built on MineRL and Project Malmo.

The source `pyproject.toml` requires Python `>=3.10` and includes dependencies such as:

- `torch>=2.3.1`
- `opencv-python`
- `opencv-python-headless`
- `gym`, `gym3`, `gymnasium`
- `ray`
- `lightning`
- `hydra-core`
- `minecraft_data==3.20.0`
- rendering and simulator-related packages such as `pyglet`, `pyopengl`, `pyrender`, and `imgui`

## Commands Attempted

```bash
export CUDA_VISIBLE_DEVICES=0
source /root/miniconda3/etc/profile.d/conda.sh
conda create -y -n minestudio-test -c conda-forge python=3.10 openjdk=8
conda run -n minestudio-test python --version
conda run -n minestudio-test java -version
timeout 900s conda run -n minestudio-test python -m pip install -q minestudio
conda run -n minestudio-test python -m pip show minestudio
conda run -n minestudio-test python -c 'import minestudio; import torch; print(torch.__version__, torch.cuda.is_available())'
conda run -n minestudio-test python -c 'from minestudio.simulator import MinecraftSim; print("MinecraftSim import ok")'
```

## Bounded Fallback

Because full dependency installation timed out, a no-deps editable install was used only to verify source packaging:

```bash
conda run -n minestudio-test python -m pip install --no-deps -e /root/autodl-tmp/external_repos/MineStudio
conda run -n minestudio-test python -m pip show minestudio
conda run -n minestudio-test python -c 'import minestudio; print("minestudio namespace import ok")'
```

Result:

```text
minestudio 1.1.5 installed in editable mode without dependencies.
Top-level namespace import passed.
```

## Issues and Fixes

### 2026-07-06: Full dependency installation timed out

- Symptom: `pip install minestudio` exited with code `124` after the 900-second timeout.
- Effect: `minestudio` was not installed through the full dependency path.
- Follow-on failures:
  - `pip show minestudio` failed before no-deps fallback.
  - `import minestudio` failed before no-deps fallback.
  - PyTorch GPU check failed because `torch` was not installed.
  - `MinecraftSim` import failed after no-deps fallback because `cv2` was not installed.
- Decision: stop the smoke test and document the blocker instead of spending hours on dependency resolution.

### Future setup idea

Try installing dependencies in smaller groups:

1. Install PyTorch with a CUDA-compatible wheel.
2. Install OpenCV and simulator imports.
3. Install the rest of MineStudio dependencies.
4. Add Xvfb or VirtualGL rendering.
5. Run `python -m minestudio.simulator.entry` with a short timeout.
