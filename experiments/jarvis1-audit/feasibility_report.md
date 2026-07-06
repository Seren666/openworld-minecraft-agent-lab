# JARVIS-1 Feasibility Report

## Summary

JARVIS-1 is important for this project, but it is not immediately runnable as a quick demo on the current AutoDL environment. The repository can be cloned and inspected, but execution requires several layers of setup: Java/MCP build, Python dependencies, OpenCV, PyTorch, Minecraft rendering, STEVE-1 weights, and possibly OpenAI API access.

This is a repository audit and feasibility check, not a complete reproduction.

## Can We Run A Minimal Demo Quickly?

Not yet.

The released quick-looking command is:

```bash
python offline_evaluation.py
```

However, even:

```bash
python offline_evaluation.py --help
```

fails before argument parsing because importing the script reaches `cv2`, which is not installed in the base environment.

The README also references:

```bash
python open_jarvis.py --task iron_pickaxe --timeout 10
```

but `open_jarvis.py` was not present in the cloned release. The README notes that only offline evaluation code is currently released.

## Required Assets And Checkpoints

The repository points to STEVE-1 weights and expects paths for:

| Asset | Expected path |
| --- | --- |
| VPT model | `jarvis/steveI/weights/vpt/2x.model` |
| STEVE-1 weights | `jarvis/steveI/weights/steve1/steve1.weights` |
| STEVE-1 prior | `jarvis/steveI/weights/steve1/steve1_prior.pt` |
| MineCLIP attention weights | `jarvis/steveI/weights/mineclip/attn.pth` |

These should be downloaded only under `/root/autodl-tmp`, not committed.

## Dependencies Likely To Break

- `torch==2.2.1` and `torchvision==0.17.1` need a CUDA-compatible install path.
- OpenCV is required early by `jarvis.assembly.marks`.
- `prepare_mcp.py` requires Java 8 plus stable downloads/build steps for MCP-Reborn.
- Minecraft simulator/rendering likely needs Xvfb or another headless rendering setup.
- `gym==0.23.1`, `gymnasium==0.29.1`, and `gym3==0.3.3` coexist in the dependency list and may require careful isolation.
- `OPENAI_API_KEY` is needed for some usage paths and must remain outside Git.

## Overlap With MC-Planner Blockers

There is strong overlap:

| Blocker | MC-Planner | JARVIS-1 |
| --- | --- | --- |
| Minecraft simulator setup | Yes | Yes |
| Controller/checkpoint assets | Yes | Yes, STEVE-1 / VPT / MineCLIP paths |
| OpenAI/API dependency | Yes | Yes |
| Rendering/headless Minecraft | Yes | Yes |
| Long dependency chain | Yes | Yes |
| Planning-only inspection possible | Yes | Partially, through fixed memory |

JARVIS-1 adds multimodal perception and memory, so the setup is broader than the DEPS / MC-Planner pass.

## Smallest Meaningful Result For Email/GitHub

The best small result is:

1. Audit repository structure and release limitations.
2. Extract fixed-memory task plans from `jarvis/assets/memory.json`.
3. Compare one fixed-memory plan with our DEPS-style dependency plan.
4. Document what an offline evaluation would require.

This would demonstrate understanding without claiming execution.

## What Was Attempted

- Cloned `https://github.com/CraftJarvis/JARVIS-1.git` under `/root/autodl-tmp/external_repos/JARVIS-1`.
- Recorded branch `main` and commit `aa9bd97debee045cb35b37564c71dee4c465b9ad`.
- Inspected README, package requirements, scripts, and expected weight paths.
- Ran safe syntax and import checks.
- Confirmed `memory.json` is readable and contains 188 fixed-memory entries.

## What Worked

- Clone succeeded.
- Repository metadata and requirements were captured.
- `offline_evaluation.py` and `prepare_mcp.py` passed syntax compilation.
- Top-level `jarvis` and `jarvis.assembly` imports worked with `PYTHONPATH`.
- Fixed-memory JSON inspection worked.

## What Remains Blocked

- No PyTorch in base AutoDL Python.
- No OpenCV in base AutoDL Python.
- No STEVE-1 weights downloaded.
- No MCP-Reborn build run.
- No Minecraft rendering setup tested.
- No OpenAI key configured.
- Online evaluation, multimodal descriptor, and multimodal retrieval are not released in the current repository.

## Recommended Next Step

Do not attempt full JARVIS-1 execution before stabilizing MineStudio or a shared Minecraft rendering stack. For the next bounded pass, create a small script that reads `memory.json` and prints fixed-memory plans for tasks like `wooden_pickaxe`, `iron_pickaxe`, and `diamond_pickaxe`. That gives useful research-email evidence without touching large assets or simulator execution.
