# JARVIS-1 Setup Notes

## Environment Policy

- External repository path: `/root/autodl-tmp/external_repos/JARVIS-1`
- Large files path: `/root/autodl-tmp`
- GPU policy: `CUDA_VISIBLE_DEVICES=0`
- No training jobs were started.
- No large checkpoints, datasets, or videos were downloaded.

## Clone

```bash
export CUDA_VISIBLE_DEVICES=0
mkdir -p /root/autodl-tmp/external_repos
cd /root/autodl-tmp/external_repos
git -c http.version=HTTP/1.1 clone --depth=1 https://github.com/CraftJarvis/JARVIS-1.git JARVIS-1
cd JARVIS-1
git remote get-url origin
git branch --show-current
git rev-parse HEAD
```

Recorded result:

```text
origin: https://github.com/CraftJarvis/JARVIS-1.git
branch: main
commit: aa9bd97debee045cb35b37564c71dee4c465b9ad
latest commit summary: aa9bd97 2024-04-08 10:48:50 +0800 Update README.md
```

## Installation Instructions Observed

The README recommends:

```bash
conda create -n jarvis python=3.10
conda activate jarvis
conda install openjdk=8
python prepare_mcp.py
pip install -e .
```

It also states that JARVIS-1 relies on STEVE-1 weights and that users need to set `TMPDIR` plus a private OpenAI API key in the runtime environment.

No API key was written to this repository.

## Python Package Requirements

The `pyproject.toml` declares:

```text
av==11.0.0
torch==2.2.1
torchvision==0.17.1
rich==13.7.1
pyyaml==6.0.1
gymnasium==0.29.1
hydra-core==1.3.2
gym==0.23.1
attrs==23.2.0
gym3==0.3.3
openai==1.16.0
```

## Checkpoints And Assets

The code expects STEVE-1 / VPT / MineCLIP-style weights at:

```text
jarvis/steveI/weights/vpt/2x.model
jarvis/steveI/weights/steve1/steve1.weights
jarvis/steveI/weights/steve1/steve1_prior.pt
jarvis/steveI/weights/mineclip/attn.pth
```

These were not downloaded.

The released fixed memory file exists:

```text
jarvis/assets/memory.json
```

Safe JSON inspection found 188 memory entries.

## Safe Checks

```bash
cd /root/autodl-tmp/external_repos/JARVIS-1
/root/miniconda3/bin/python -m py_compile offline_evaluation.py prepare_mcp.py
```

Result:

```text
py_compile exit code: 0
```

```bash
PYTHONPATH=/root/autodl-tmp/external_repos/JARVIS-1 \
  /root/miniconda3/bin/python - <<'PY'
import jarvis
import jarvis.assembly
print("imports ok")
PY
```

Result:

```text
import jarvis ok
import jarvis.assembly ok
```

```bash
PYTHONPATH=/root/autodl-tmp/external_repos/JARVIS-1 \
  /root/miniconda3/bin/python offline_evaluation.py --help
```

Result:

```text
ModuleNotFoundError: No module named 'cv2'
```

The help command fails before argparse because module imports require OpenCV.

## Execution Notes

`offline_evaluation.py` constructs a Minecraft wrapper and render wrapper after parsing arguments, so running it is not a lightweight check once dependencies exist. It should only be run after simulator/rendering setup is intentionally prepared.

`prepare_mcp.py` invokes shell scripts, Gradle, Minecraft asset downloads, and MCP-Reborn build steps. It was not run during this bounded audit.
