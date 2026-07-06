# JARVIS-1

## Reading Status

Bounded repository audit and feasibility check completed on 2026-07-06.

## Problem

JARVIS-1 studies open-world multi-task agents in Minecraft. The core challenge is not only planning a task sequence, but also connecting human instructions, visual observations, memory, and embodied control in a long-horizon environment with sparse feedback.

## Key System Idea

JARVIS-1 combines:

- Multimodal input from visual observations and human instructions
- A memory-augmented multimodal language model for planning
- Task memory for fixed-memory offline evaluation
- Embodied control through Minecraft skills and STEVE-1-style controller components
- Minecraft simulator execution through the released environment stack

The released repository currently exposes enough structure to inspect the system, but not enough to claim a complete reproduction.

## Relationship To DEPS

DEPS focuses on interactive planning, dependency reasoning, failure explanation, replanning, and subgoal selection. JARVIS-1 extends the research direction toward a more integrated agent: multimodal perception, memory, language planning, and embodied control.

In this repository, DEPS is useful as the first planning baseline, while JARVIS-1 is central because it ties that planning problem to perception, memory, and action.

## Upstream Implementation Inspected

| Item | Value |
| --- | --- |
| Repository | `https://github.com/CraftJarvis/JARVIS-1.git` |
| Branch | `main` |
| Commit | `aa9bd97debee045cb35b37564c71dee4c465b9ad` |
| AutoDL external path | `/root/autodl-tmp/external_repos/JARVIS-1` |

## What We Attempted

- Cloned the official CraftJarvis JARVIS-1 repository under `/root/autodl-tmp/external_repos`.
- Inspected README, `pyproject.toml`, `offline_evaluation.py`, `prepare_mcp.py`, and controller/path files.
- Recorded Python, Java, PyTorch, Minecraft, STEVE-1 weights, and OpenAI API requirements.
- Ran safe checks only:
  - repository metadata
  - file and asset size inspection
  - script syntax compilation for `offline_evaluation.py` and `prepare_mcp.py`
  - top-level package import with `PYTHONPATH`
  - `offline_evaluation.py --help` as a safe non-execution check
  - fixed-memory JSON summary
- Created a separate `jarvis1-runtime-test` environment for bounded runtime checks.
- Built an original toy memory-augmented planning demo to illustrate the memory idea without using official model weights or raw memory entries.

## What Worked

- The repository cloned successfully on AutoDL.
- `py_compile` passed for `offline_evaluation.py` and `prepare_mcp.py`.
- `import jarvis` and `import jarvis.assembly` worked with `PYTHONPATH` before installing the package.
- The released fixed-memory file was readable and contained 188 memory entries.
- Aggregate fixed-memory analysis showed 188 entries, 1399 plan steps, and mostly `craft`, `mine`, and `smelt` step types.
- The toy memory planner generated structured traces for iron ingot, stone sword, shelter, and diamond-with-insufficient-tools tasks.

## What Can Be Realistically Reproduced

Short term:

- Repository audit and architecture summary
- Fixed-memory inspection
- Task/memory plan extraction
- Dependency and environment preparation notes
- Possibly a package install/import smoke test after installing OpenCV, PyTorch, and Java/MCP dependencies
- A local memory-augmented planning demonstration that compares plans with and without retrieved memory

Medium term:

- One offline evaluation attempt with a short timeout, only after:
  - `prepare_mcp.py` succeeds
  - OpenJDK 8 is confirmed
  - PyTorch and OpenCV are installed
  - STEVE-1 weights are downloaded under `/root/autodl-tmp`
  - rendering is configured with Xvfb or equivalent
  - `OPENAI_API_KEY` is available outside Git if the chosen path needs it

## What Remains Blocked

- Official-style `torch==2.2.1+cu121` detects the Blackwell GPU but cannot execute tensor kernels because the wheel supports architectures up to `sm_90`, while the GPU is `sm_120`.
- A newer CUDA 12.8 PyTorch install attempt failed because the root filesystem ran out of space.
- `offline_evaluation.py --help` still fails before a useful help screen after small dependency installs; the observed dependency chain reached `coloredlogs`, `psutil`, `daemoniker`, and then `lxml`.
- Installing `av==11.0.0` failed because FFmpeg development libraries were missing.
- `prepare_mcp.py` likely requires a stable network and Gradle/Minecraft asset downloads.
- STEVE-1 weights are required and were not downloaded.
- The README requires `OPENAI_API_KEY` for agent usage.
- The released repository notes that online evaluation, multimodal descriptor, and multimodal retrieval are not released yet.
- `open_jarvis.py` mentioned in README was not present in the cloned release.

## Memory As A Research Entry Point

The fixed-memory file is a good bounded entry point because it exposes the high-level planning structure without requiring Minecraft rendering or large checkpoints. The observed memory entries are task-level rather than raw action traces, and they mainly encode reusable crafting, mining, and smelting sequences.

This connects directly to the research question: how should an embodied Minecraft agent retrieve and trust prior experience when planning a long-horizon task? The lightweight demo in `experiments/jarvis1-memory-demo/` uses toy memory to show both the benefit and the risk: memory can add missing prerequisites, but irrelevant or stale memory can push the plan toward wrong subgoals.

## Why This Paper Is Central

JARVIS-1 is central to this research direction because it moves beyond text-only planning. It connects high-level language reasoning with multimodal state, memory, and Minecraft control. That makes it a natural bridge from DEPS-style planning notes to later work such as GROOT, OmniJARVIS, ROCKET-style policies, and MineStudio-based benchmark evaluation.

## Reproduction Angle

For email outreach, the strongest honest artifact is a feasibility report plus a small fixed-memory analysis and original memory-augmented planning demo. A full reproduction should be deferred until simulator setup, dependencies, controller weights, CUDA compatibility, and rendering are stable.
