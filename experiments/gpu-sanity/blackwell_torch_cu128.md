# Blackwell PyTorch CUDA 12.8 Test

This is infrastructure evidence only. It is not a ROCKET-1, JARVIS-1, or MineStudio reproduction.

## Goal

Check whether a modern PyTorch CUDA build can execute a tiny tensor workload on the AutoDL Blackwell GPU without modifying existing pinned reproduction environments.

## Environment Policy

| Item | Value |
| --- | --- |
| Conda environment prefix | `/root/autodl-tmp/conda_envs/blackwell-torch-test` |
| Conda package cache | `/root/autodl-tmp/conda_pkgs` |
| Pip cache | `/root/autodl-tmp/pip_cache` |
| Temporary directory | `/root/autodl-tmp/tmp` |
| GPU policy | `CUDA_VISIBLE_DEVICES=0` |
| Raw log location | `/root/autodl-tmp/logs/blackwell_torch_cu128_2026-07-06.log` |

Large install artifacts were kept under `/root/autodl-tmp` and were not committed.

## Commands

```bash
export CUDA_VISIBLE_DEVICES=0
export CONDA_PKGS_DIRS=/root/autodl-tmp/conda_pkgs
export PIP_CACHE_DIR=/root/autodl-tmp/pip_cache
export TMPDIR=/root/autodl-tmp/tmp

conda create -y -p /root/autodl-tmp/conda_envs/blackwell-torch-test python=3.10 pip
/root/autodl-tmp/conda_envs/blackwell-torch-test/bin/python \
  -m pip install --index-url https://download.pytorch.org/whl/cu128 torch torchvision

CUDA_VISIBLE_DEVICES=0 /root/autodl-tmp/conda_envs/blackwell-torch-test/bin/python - <<'PY'
import torch
print("torch", torch.__version__)
print("cuda_available", torch.cuda.is_available())
print("device", torch.cuda.get_device_name(0))
print("arch_list", torch.cuda.get_arch_list())
x = torch.randn(1024, 1024, device="cuda")
y = x @ x
torch.cuda.synchronize()
print("mean", y.mean().item())
PY
```

## Result

```text
Python 3.10.20
torch 2.11.0+cu128
cuda_available True
device NVIDIA RTX PRO 6000 Blackwell Server Edition
arch_list ['sm_75', 'sm_80', 'sm_86', 'sm_90', 'sm_100', 'sm_120']
mean -0.011088745668530464
```

The tensor workload completed successfully.

## Disk Result

```text
/root/autodl-tmp size: 550G
/root/autodl-tmp used after install: 12G
environment size: 6.9G
pip cache size: 3.8G
```

## Interpretation

The previous JARVIS-1 pinned `torch==2.2.1+cu121` stack failed because it did not include `sm_120` kernels. A modern `torch 2.11.0+cu128` wheel does include `sm_120` and can run a small CUDA workload on this machine.

Future ROCKET-1 or MineStudio attempts should use a compatible modern PyTorch stack where the official code allows it. This does not remove simulator, checkpoint, SAM-2, rendering, or dependency blockers.
