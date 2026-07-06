# GPU Sanity Check

This folder records infrastructure checks for the AutoDL GPU environment. It is not a research result and does not run model training.

## Purpose

The current AutoDL machine has powerful Blackwell GPUs. Before attempting Minecraft agent workloads, the repository records whether a Python ML stack can actually execute a small CUDA tensor workload.

## Files

| File | Purpose |
| --- | --- |
| `gpu_check.py` | Small PyTorch CUDA sanity script |
| `gpu_check_log.md` | Summary of the bounded AutoDL GPU check |
| `blackwell_torch_cu128.md` | Successful modern PyTorch CUDA 12.8 test under `/root/autodl-tmp` |

## Run

On AutoDL, after installing a compatible PyTorch build:

```bash
export CUDA_VISIBLE_DEVICES=0
python experiments/gpu-sanity/gpu_check.py
```

The script writes a compact Markdown log by default. It does not download data, load model weights, or run training.

## Current Finding

The old JARVIS-1 pinned `torch 2.2.1+cu121` stack detects the Blackwell GPU but cannot execute kernels. A separate `torch 2.11.0+cu128` environment under `/root/autodl-tmp` does support `sm_120` and passed a tiny CUDA tensor workload.
