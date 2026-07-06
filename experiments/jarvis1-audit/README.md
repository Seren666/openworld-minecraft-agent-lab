# JARVIS-1 Repository Audit

This folder records a bounded JARVIS-1 repository audit and feasibility check. It is not a complete reproduction, not a training run, and not a claim of official benchmark results.

## Goal

Determine what can realistically be run on the current AutoDL machine and identify the smallest useful evidence artifact for a research email.

## Upstream Repository

| Item | Value |
| --- | --- |
| Repository | `https://github.com/CraftJarvis/JARVIS-1.git` |
| Branch | `main` |
| Commit | `aa9bd97debee045cb35b37564c71dee4c465b9ad` |
| External path | `/root/autodl-tmp/external_repos/JARVIS-1` |

External code, large assets, checkpoints, datasets, raw logs, and videos stay outside this GitHub repository.

## What Was Inspected

- README
- `pyproject.toml`
- `offline_evaluation.py`
- `prepare_mcp.py`
- `jarvis/steveI/path.py`
- Released fixed memory at `jarvis/assets/memory.json`
- Top-level scripts and package layout

## Safe Checks Run

- Shallow clone under `/root/autodl-tmp/external_repos`
- Repository metadata and file-size inspection
- Syntax compilation of `offline_evaluation.py` and `prepare_mcp.py`
- Base Python CUDA/PyTorch availability check
- `PYTHONPATH` package import check
- `offline_evaluation.py --help` check with a short timeout
- Fixed-memory JSON summary

## Main Result

A minimal demo is not immediately ready on the current machine. The repository is inspectable, but useful execution requires dependency installation, OpenCV, PyTorch, MCP/Minecraft setup, STEVE-1 weights, and likely rendering configuration.

The smallest meaningful email/GitHub artifact is a transparent feasibility report plus a fixed-memory planning inspection, not an end-to-end Minecraft run.
