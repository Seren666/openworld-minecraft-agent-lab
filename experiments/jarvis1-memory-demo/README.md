# JARVIS-1 Memory Demo

This folder contains a lightweight JARVIS-1-style memory-augmented planning demo. It is not an official JARVIS-1 reproduction and does not run Minecraft, load checkpoints, or copy the official memory file into this repository.

## Purpose

JARVIS-1 is relevant to this project because it connects high-level planning with multimodal observations, embodied control, and memory. The official system is too heavy for a quick bounded reproduction pass, but the released repository includes a fixed memory file that can be inspected safely.

This demo focuses on the memory idea:

- inspect the official memory file only through aggregate statistics
- build a small original toy memory set
- retrieve relevant memories for common Minecraft tasks
- compare planning traces with and without memory

## Files

| File | Purpose |
| --- | --- |
| `memory_analysis.md` | Aggregate analysis of the official JARVIS-1 fixed-memory file |
| `memory_stats.py` | Safe aggregate-only analyzer for the external memory file |
| `demo_memory.json` | Small original toy memory entries |
| `demo_tasks.json` | Small original task states |
| `memory_augmented_planner.py` | Local planning demo with lightweight retrieval |
| `logs/example_run.md` | Generated example planning trace |

## Tasks

The demo covers four bounded tasks:

1. obtain iron ingot
2. craft stone sword
3. build a small shelter
4. obtain diamond with insufficient tools

## Run

From the repository root:

```bash
python experiments/jarvis1-memory-demo/memory_augmented_planner.py
```

On the AutoDL machine, aggregate-only official memory stats can be collected with:

```bash
python experiments/jarvis1-memory-demo/memory_stats.py \
  --path /root/autodl-tmp/external_repos/JARVIS-1/jarvis/assets/memory.json
```

## What This Demonstrates

The demo shows how retrieved task memory can change a plan by adding missing preconditions, tool-level constraints, safety timing, and smelting requirements. For example, a memory about wooden pickaxes failing on iron ore should push the planner toward crafting a stone pickaxe first.

## Limitations

- No official JARVIS-1 model is loaded.
- No Minecraft simulator is started.
- No STEVE-1, VPT, MineCLIP, or checkpoint assets are used.
- The retrieval method is intentionally simple and local.
- The generated plans are illustrative, not measured task success.

This is useful as a research-entry artifact, not as a claim of complete reproduction.
