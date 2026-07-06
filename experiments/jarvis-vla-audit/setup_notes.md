# JARVIS-VLA Setup Notes

## Clone

The clone was performed under the AutoDL data disk, not the small system disk.

```bash
export CUDA_VISIBLE_DEVICES=0
export CONDA_PKGS_DIRS=/root/autodl-tmp/conda_pkgs
export PIP_CACHE_DIR=/root/autodl-tmp/pip_cache
export TMPDIR=/root/autodl-tmp/tmp

mkdir -p /root/autodl-tmp/external_repos
cd /root/autodl-tmp/external_repos
git -c http.version=HTTP/1.1 clone https://github.com/CraftJarvis/JarvisVLA.git JarvisVLA
cd JarvisVLA
git remote get-url origin
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD
```

Recorded result:

```text
origin: https://github.com/CraftJarvis/JarvisVLA.git
branch: master
commit: 0aafd2ed0ba9270f40d710440ca70cdc3fa48a11
repository size on data disk: 125M
```

## README Installation Path

The official README describes:

```bash
git clone https://github.com/CraftJarvis/JarvisVLA.git
conda create -n mcvla python=3.10
conda activate mcvla
cd JarvisVLA
conda install --channel=conda-forge openjdk=8 -y
pip install -e .
```

It then suggests checking MineStudio simulator setup:

```bash
python -m minestudio.simulator.entry
MINESTUDIO_GPU_RENDER=1 python -m minestudio.simulator.entry
```

## Requirements Observed

The repository `requirements.txt` includes:

```text
minestudio
accelerate==1.2.1
av==14.1.0
datasets
deepspeed==0.16.3
huggingface-hub==0.28.1
numpy==1.26.4
opencv-python
opencv-python-headless
peft==0.14.0
qwen-vl-utils
ray
torch
torchaudio
torchvision
transformers
trl
vllm
wandb
```

This is a heavy VLA and simulator stack, not a quick import-only dependency list.

## Inference Path

The README serves the model with vLLM:

```bash
CUDA_VISIBLE_DEVICES=0 vllm serve jarvis_vla_qwen2_vl_7b_sft --port 8000
sh scripts/evaluate/rollout-kill.sh
```

The rollout scripts call `jarvisvla/evaluate/evaluate.py` with settings such as:

```text
workers=5
max_frames=300-500
history_num=2-4
action_chunk_len=1
model_local_path=/nfs-shared/models/JarvisVLA-Qwen2-VL-7B
```

These are not lightweight checks. They require model serving, MineStudio/Minecraft simulation, and likely video/log output.

## Safe Checks Run

```bash
cd /root/autodl-tmp/external_repos/JarvisVLA
python -m py_compile $(find . -maxdepth 4 -name '*.py' | head -n 25)
```

Result:

```text
py_compile_exit: 0
```

No training, model serving, dataset download, model checkpoint download, simulator launch, or rollout was started.

## Blackwell PyTorch Context

The existing data-disk environment was checked:

```text
/root/autodl-tmp/conda_envs/blackwell-torch-test
torch 2.11.0+cu128
cuda_available True
device NVIDIA RTX PRO 6000 Blackwell Server Edition
arch_list includes sm_120
```

This environment is suitable for small toy GPU checks, but it does not make official JARVIS-VLA reproduction complete.
