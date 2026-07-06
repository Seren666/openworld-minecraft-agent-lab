# JARVIS-1 Runtime Check

This file records a bounded runtime feasibility check for the official JARVIS-1 repository. It is not a full reproduction, simulator run, checkpoint load, or Minecraft evaluation.

## Scope

| Item | Value |
| --- | --- |
| External repository | `/root/autodl-tmp/external_repos/JARVIS-1` |
| Upstream URL | `https://github.com/CraftJarvis/JARVIS-1.git` |
| Branch | `main` |
| Commit | `aa9bd97debee045cb35b37564c71dee4c465b9ad` |
| Conda environment | `jarvis1-runtime-test` |
| Python | `3.10.20` |
| GPU policy | `CUDA_VISIBLE_DEVICES=0` |

## GPU Snapshot

The AutoDL machine exposes six GPUs:

```text
NVIDIA RTX PRO 6000 Blackwell Server Edition
GPU memory per device: 97887 MiB
Driver version: 595.71.05
NVIDIA-SMI reported CUDA version: 13.2
```

No training or evaluation job was started. GPU memory was idle before the checks.

## Installed Runtime Pieces

The bounded runtime environment installed the official-style JARVIS PyTorch stack and small dependencies:

```text
torch==2.2.1+cu121
torchvision==0.17.1+cu121
opencv-python-headless==4.11.0
rich
pyyaml
gymnasium==0.29.1
hydra-core==1.3.2
gym==0.23.1
attrs==23.2.0
gym3==0.3.3
openai==1.16.0
coloredlogs
psutil
daemoniker
```

Installing `av==11.0.0` failed because system FFmpeg/pkg-config libraries were missing for `libavdevice`, `libavfilter`, `avformat`, `avcodec`, `avutil`, `swscale`, and `swresample`.

## PyTorch CUDA Result

```text
torch: 2.2.1+cu121
cuda_available: True
device: NVIDIA RTX PRO 6000 Blackwell Server Edition
supported_arch_list: sm_50, sm_60, sm_70, sm_75, sm_80, sm_86, sm_90
tensor_workload: failed
```

The tensor workload failed with:

```text
RuntimeError: CUDA error: no kernel image is available for execution on the device
```

Interpretation: the official pinned PyTorch stack can see the Blackwell GPU, but the wheel does not include `sm_120` kernels. This blocks GPU-backed JARVIS runtime checks on this machine unless the PyTorch stack is updated to a build that supports Blackwell.

## Script Checks

| Check | Result |
| --- | --- |
| `import jarvis` | Passed |
| `import jarvis.assembly` | Passed |
| `import cv2` | Passed, version `4.11.0` |
| `offline_evaluation.py --help` before extra deps | Blocked by missing `coloredlogs` |
| after `coloredlogs` | Blocked by missing `psutil` |
| after `psutil` | Blocked by missing `daemoniker` |
| after `daemoniker` | Blocked by missing `lxml` |
| `prepare_mcp.py --help` | Timed out after 60 seconds |

The repeated `--help` blockers happen before a useful argparse/help screen. This confirms that even help-mode imports enter the simulator dependency chain.

## Remaining Blockers

- Official pinned PyTorch does not execute CUDA kernels on the Blackwell `sm_120` GPU.
- Newer CUDA/PyTorch installation attempt failed because the root filesystem had insufficient free space.
- `av==11.0.0` needs system FFmpeg development libraries.
- `offline_evaluation.py` still requires additional simulator dependencies after `coloredlogs`, `psutil`, and `daemoniker`.
- `prepare_mcp.py` appears to perform setup/build work rather than a lightweight help command.
- No STEVE-1, VPT, MineCLIP, or controller checkpoints were downloaded.
- No OpenAI API key was configured.
- No Minecraft rendering path was prepared.

## Feasibility Conclusion

Official JARVIS-1 evaluation is not worth pursuing before the first research email. The useful bounded result is the repository audit plus fixed-memory analysis and a local memory-augmented planning demo. A future official run should first solve the Blackwell-compatible PyTorch stack, FFmpeg/`av`, Java/MCP build, rendering, and checkpoint path issues.
