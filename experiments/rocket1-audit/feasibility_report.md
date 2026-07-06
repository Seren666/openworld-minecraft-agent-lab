# ROCKET-1 Feasibility Report

## Summary

ROCKET-1 is relevant and inspectable, but official inference is not a quick bounded reproduction on the current AutoDL setup. The smallest useful result before email outreach is a repository audit plus a lightweight local visual/mask prompting demo.

## Can We Run A Minimal Official Demo Quickly?

Not without additional setup.

The README's usage snippet is compact, but it depends on a model loaded from Hugging Face, CUDA execution, segmentation masks, and action conversion through the Minecraft wrapper. The Gradio path also expects SAM-2 checkpoints and a Minecraft environment.

The documented simulator check requires MCP-Reborn for Minecraft 1.16.5, OpenJDK 8, rendering/system libraries, and a working Python dependency stack.

## Required Assets

| Asset | Purpose | Status |
| --- | --- | --- |
| ROCKET-1 model weights from `phython96/ROCKET-1` | policy inference | Not downloaded |
| SAM-2 checkpoints | segmentation and mask tracking | Not downloaded |
| MCP-Reborn.zip from `phython96/ROCKET-MCP-Reborn` | Minecraft simulator | Not downloaded |
| Rendering/system libraries | Minecraft environment | Not installed in this sprint |

## Dependency Risks

- The dependency list overlaps with previous JARVIS-1 and MineStudio blockers: OpenCV, `av`, gym variants, Java, Minecraft simulator, rendering, and model weights.
- Root filesystem pressure remains high, so large installs must stay under `/root/autodl-tmp`.
- ROCKET-1's root package does not pin an exact PyTorch version, but its SAM-2 subpackage requires `torch>=2.3.1`.
- The older JARVIS pinned stack failed on the Blackwell GPU; ROCKET-1 should use a modern Blackwell-compatible PyTorch build if official inference is attempted later.

## Blackwell Compatibility

A separate infrastructure test showed that `torch 2.11.0+cu128` installed under `/root/autodl-tmp` can execute a small CUDA tensor workload on the RTX PRO 6000 Blackwell GPU and reports support for `sm_120`.

This helps future ROCKET-1 setup, but it is not a ROCKET-1 result.

## What Can Be Reproduced Before Email Outreach?

Safe and useful:

- Explain the visual-temporal context prompting idea.
- Audit official repository requirements and release structure.
- Build a small original toy demo comparing language-only instructions to mask/interaction prompts.
- Connect ROCKET-1 to earlier DEPS/JARVIS-1 notes.

Not worth forcing now:

- Full Minecraft simulator launch.
- SAM-2 checkpoint download and realtime segmentation.
- ROCKET-1 model checkpoint download.
- Gradio demo with live Minecraft interaction.
- Any training or evaluation job.

## Relationship To Existing Blockers

| Blocker | Seen in earlier tasks | Applies to ROCKET-1 |
| --- | --- | --- |
| Minecraft simulator setup | MC-Planner, JARVIS-1, MineStudio | Yes |
| Rendering/headless environment | MC-Planner, JARVIS-1, MineStudio | Yes |
| Model/checkpoint assets | MC-Planner, JARVIS-1 | Yes |
| OpenCV and `av` dependencies | JARVIS-1, MineStudio | Yes |
| Blackwell PyTorch compatibility | JARVIS-1 | Solved separately with modern cu128 test, but not integrated |

## Conclusion

For the first advisor email, the honest artifact is the audit plus a toy visual prompt demo. Official ROCKET-1 execution should be deferred until the simulator, SAM-2 checkpoints, model weights, and modern PyTorch environment are intentionally prepared.
