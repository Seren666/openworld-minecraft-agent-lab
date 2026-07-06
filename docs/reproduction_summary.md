# Reproduction Summary

| Experiment | Status | Output | Notes |
| --- | --- | --- | --- |
| DEPS / MC-Planner | Bounded planning pass complete | Upstream inspection, Conda env creation, planning-only task examples | Official demo blocked by OpenAI keys, controller checkpoint, modified MineDojo / MC-Simulator, and Minecraft rendering setup. |
| MineStudio setup | Smoke test blocked by dependency install timeout | Official repo cloned, `minestudio-test` env created, Python/OpenJDK verified, no-deps package import verified | Full `pip install minestudio` timed out after 900 seconds; PyTorch/OpenCV/simulator checks remain unresolved. |
| JARVIS-1 audit | Bounded feasibility check complete | Official repo cloned, requirements inspected, syntax/import checks run, fixed-memory file inspected | Minimal demo not ready: requires OpenCV, PyTorch, MCP/Minecraft setup, STEVE-1 weights, rendering, and possibly OpenAI API access. |
| Minecraft task analysis | In progress | Taxonomy and failure notes | Use as shared vocabulary for demos. |
| Mini VLA gridworld | Planned | Small sandbox results | Keep compute requirements low. |

## Evidence Rules

- Keep commands and environment details in Markdown.
- Commit only small screenshots that clarify results.
- Do not commit checkpoints, datasets, raw videos, large logs, or generated output folders.
