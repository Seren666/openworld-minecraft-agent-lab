# JARVIS-VLA Feasibility Report

## Summary

JARVIS-VLA is highly relevant to this repository because it explicitly bridges VLMs and game actions. It is also too heavy for a quick bounded official run: the released path depends on MineStudio, vLLM serving, a Qwen2-VL-7B-scale model, dataset/model assets, and Minecraft rollout.

The best pre-email artifact is an audit plus a lightweight action-interface demo.

## Can We Run A Minimal Official Demo Quickly?

Not without additional assets and setup.

The inference path requires:

- a model served through vLLM
- JARVIS-VLA model weights from Hugging Face or a local model path
- MineStudio simulator installation
- Java/OpenJDK 8
- rendering through Xvfb or VirtualGL
- evaluation scripts that can run multiple workers and hundreds of frames

This exceeds the sprint's bounded goal.

## Model And Dataset Requirements

| Item | Source | Status |
| --- | --- | --- |
| JARVIS-VLA model collection | `https://huggingface.co/collections/CraftJarvis/jarvis-vla-v1-67dc157a99d011efd7d7f7e4` | Not downloaded |
| Minecraft VLA SFT dataset | `https://huggingface.co/datasets/CraftJarvis/minecraft-vla-sft` | Not downloaded |
| Qwen2-VL base/model stack | implied by scripts and requirements | Not downloaded |
| MineStudio simulator assets | required through `minestudio` | Not installed for official run |

No large model weights, datasets, checkpoints, raw videos, or simulator outputs were downloaded or committed.

## Dependency Risks

- MineStudio remains partially blocked in this repository's earlier smoke tests.
- vLLM and Qwen2-VL serving are heavy and need careful GPU/runtime compatibility.
- `av`, OpenCV, Ray, DeepSpeed, and simulator rendering add known environment risk.
- Official evaluation scripts can generate large logs/videos and should write only under `/root/autodl-tmp`.
- The system disk is small, so all future environments, caches, temp files, and outputs should stay on `/root/autodl-tmp`.

## Blackwell Suitability

The modern data-disk PyTorch environment is promising:

```text
torch 2.11.0+cu128
Blackwell sm_120 supported
small CUDA tensor workload succeeded in prior GPU sanity test
```

This suggests the GPU can support future VLA experiments if the rest of the stack is installed with a compatible modern PyTorch setup. It does not prove official JARVIS-VLA inference works.

## What Can Be Reproduced Before Email Outreach?

Safe and useful:

- Explain the action-oriented VLA formulation.
- Audit repository dependencies and official inference path.
- Build a toy action-interface demo:
  vision-language observation + task instruction + action space -> structured action.
- Optionally run a tiny GPU scorer on toy feature vectors.

Not worth forcing now:

- vLLM serving of a 7B model.
- official rollout with MineStudio.
- model/data checkpoint download.
- training or fine-tuning.

## Conclusion

JARVIS-VLA should be presented as the next conceptual step after DEPS, JARVIS-1, and ROCKET-1: it turns perception and language into game actions. Official reproduction should wait until MineStudio, model weights, vLLM, storage, and rendering are deliberately prepared.
