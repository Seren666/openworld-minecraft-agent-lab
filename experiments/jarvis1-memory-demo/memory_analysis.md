# JARVIS-1 Memory Analysis

This note summarizes a bounded inspection of the official JARVIS-1 fixed-memory file at:

```text
/root/autodl-tmp/external_repos/JARVIS-1/jarvis/assets/memory.json
```

The raw file was not copied into this repository.

## Aggregate Findings

| Item | Result |
| --- | --- |
| Top-level JSON type | `dict` |
| Number of entries | 188 |
| Common entry fields | `time`, `status`, `image`, `init_inventory`, `plan` |
| Entries with `plan` | 188 |
| Total plan steps | 1399 |
| Plan length | min 1, max 16, average 7.44 |

## Plan Step Schema

The inspected plan steps consistently exposed these fields:

| Field | Count |
| --- | ---: |
| `goal` | 1399 |
| `type` | 1399 |
| `text` | 1399 |

The step `type` values were mostly:

| Step type | Count |
| --- | ---: |
| `craft` | 881 |
| `mine` | 438 |
| `smelt` | 80 |

## What The Entries Contain

The memory entries look primarily task-level and crafting/mining-oriented. They encode compact plans for Minecraft item acquisition and construction-like objectives. The sampled task names include common survival and crafting targets such as wood products, tools, glass, stone, pickaxes, and other recipes.

The file does not look like raw low-level action traces. It is closer to fixed task memory: previous high-level subgoal plans, initial inventory assumptions, and structured crafting or mining steps.

## Relationship To JARVIS-1

JARVIS-1 uses memory as part of a memory-augmented planning pipeline. For an open-world Minecraft agent, memory can provide reusable prior experience: what items are prerequisites, which tool levels are valid, when smelting is required, and which subgoals commonly appear before a target item.

This matters because long-horizon Minecraft tasks are sparse and compositional. An agent that forgets that iron requires stone tools, or that smelting requires both ore and fuel, can waste many steps before receiving a useful failure signal.

## Why Memory Matters

Memory can help with:

- retrieving prior plans for similar target items
- avoiding repeated failed tool choices
- adding missing crafting-table, furnace, or fuel prerequisites
- stabilizing long-horizon planning when the current observation is incomplete
- connecting DEPS-style symbolic dependencies with JARVIS-1-style embodied execution

## Risks

Memory can also hurt planning:

- stale memory: old plans may assume a different environment or inventory
- irrelevant memory: retrieved entries can match keywords but not the real task
- wrong retrieval: a related item may have different tool or recipe constraints
- overly abstract memory: high-level steps may omit timing, pathing, or safety details
- conflict with current state: memory may suggest crafting tools already available, or mining resources absent from the biome

## Reproduction Interpretation

This analysis is lightweight and evidence-based. It supports a research email by showing that the released JARVIS-1 memory artifact can be inspected and connected to planning behavior, but it does not reproduce official JARVIS-1 evaluation.
