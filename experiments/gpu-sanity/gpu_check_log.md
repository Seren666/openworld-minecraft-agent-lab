# GPU Check Log

This is an infrastructure check, not a research result.

## AutoDL GPU Snapshot

| Item | Result |
| --- | --- |
| GPU count | 6 |
| GPU model | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| Memory per GPU | 97887 MiB |
| Driver version | 595.71.05 |
| NVIDIA-SMI CUDA version | 13.2 |
| GPU policy for tests | `CUDA_VISIBLE_DEVICES=0` |

## JARVIS Runtime PyTorch Check

The `jarvis1-runtime-test` environment used:

```text
torch 2.2.1+cu121
```

PyTorch reported:

```text
cuda_available: True
device: NVIDIA RTX PRO 6000 Blackwell Server Edition
supported architectures: sm_50, sm_60, sm_70, sm_75, sm_80, sm_86, sm_90
```

The tiny tensor workload failed:

```text
RuntimeError: CUDA error: no kernel image is available for execution on the device
```

Interpretation: the installed PyTorch wheel does not support the Blackwell `sm_120` architecture.

## Newer PyTorch Attempt

A separate `gpu-sanity-test` environment attempted to install a newer CUDA 12.8 PyTorch wheel:

```bash
python -m pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cu128 torch torchvision
```

The install failed:

```text
ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device
```

## Conclusion

The hardware is available, but a GPU-backed PyTorch experiment was not completed in this sprint. The next infrastructure step is to free or expand root filesystem space, then install a Blackwell-compatible PyTorch build before attempting any model or simulator workload.
