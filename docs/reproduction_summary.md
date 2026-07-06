# Reproduction Summary

| Experiment | Status | Output | Notes |
| --- | --- | --- | --- |
| DEPS / MC-Planner | Bounded planning pass complete | Upstream inspection, Conda env creation, planning-only task examples | Official demo blocked by OpenAI keys, controller checkpoint, modified MineDojo / MC-Simulator, and Minecraft rendering setup. |
| MineStudio setup | Second-pass install still blocked | Official repo cloned, `minestudio-test` env created, no-deps package import verified, bounded dependency dry-run attempted | Full dependency setup remains unresolved; PyTorch/OpenCV/simulator imports are blocked. |
| JARVIS-1 audit | Runtime feasibility check complete | Official repo cloned, requirements inspected, syntax/import checks run, fixed-memory file inspected, runtime env tested | Minimal official demo is blocked by Blackwell/PyTorch compatibility, simulator dependencies, MCP, checkpoints, rendering, and possibly OpenAI API access. |
| JARVIS-1 memory demo | Lightweight local demo complete | Aggregate memory stats plus original toy memory-augmented planner and generated Markdown trace | Useful research-entry evidence; not an official JARVIS-1 reproduction. |
| GPU sanity | Hardware visible, PyTorch workload blocked | GPU snapshot and tiny tensor test recorded | Six Blackwell GPUs are visible, but the official pinned PyTorch wheel lacks `sm_120` kernels; a newer CUDA wheel install failed due root filesystem space. |
| Minecraft task analysis | In progress | Taxonomy and failure notes | Use as shared vocabulary for demos. |
| Mini VLA gridworld | Planned | Small sandbox results | Keep compute requirements low. |

## Completed Lightweight Work

- DEPS-style planning demo with prompts, task examples, and Markdown logs.
- JARVIS-1 repository audit and feasibility report.
- Aggregate-only analysis of the official JARVIS-1 fixed-memory file.
- Original toy memory-augmented planner for four Minecraft tasks.
- MineStudio source/package smoke checks without downloading datasets or checkpoints.
- GPU infrastructure notes for the AutoDL Blackwell machine.

## Partially Blocked Official Systems

- MC-Planner and JARVIS-1 both require simulator setup, controller/checkpoint assets, rendering, and possibly API keys.
- JARVIS-1 official-style `torch==2.2.1+cu121` sees the GPU but cannot execute kernels on Blackwell `sm_120`.
- MineStudio full dependency setup did not complete in bounded passes; top-level no-deps import works, but simulator imports need OpenCV, PyTorch, Java/PATH cleanup, and rendering dependencies.

## Safe To Mention In Email

- I cloned and audited official repositories under `/root/autodl-tmp/external_repos`.
- I avoided pushing external source code, model weights, datasets, raw videos, and secrets.
- I built lightweight planning and memory demos to show understanding of long-horizon Minecraft dependencies.
- I identified concrete blockers for official evaluation: CUDA/PyTorch architecture mismatch, simulator stack, assets, rendering, and dependency installation.

## Do Not Overstate

- Do not claim full reproduction of DEPS, JARVIS-1, or MineStudio.
- Do not claim official Minecraft task success.
- Do not claim GPU-backed model execution until a Blackwell-compatible PyTorch stack passes a tensor workload.
- Do not imply official JARVIS-1 memory was copied or modified in this repository.

## Next Recommended Experiment

Run a small comparison between the DEPS-style planner and the toy JARVIS-1-style memory planner on the same task set. This is low-cost, email-relevant, and does not require simulator rendering or large assets.

## Evidence Rules

- Keep commands and environment details in Markdown.
- Commit only small screenshots that clarify results.
- Do not commit checkpoints, datasets, raw videos, large logs, or generated output folders.
