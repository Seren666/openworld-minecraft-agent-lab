#!/usr/bin/env bash
set -euo pipefail

demo="${1:-deps-planner-demo}"

case "$demo" in
  deps-planner-demo)
    echo "DEPS planner demo scaffold is ready at experiments/deps-planner-demo"
    echo "Add prompts under experiments/deps-planner-demo/prompts before running a planner script."
    ;;
  mini-vla-gridworld)
    echo "Mini VLA gridworld scaffold is ready at experiments/mini-vla-gridworld"
    echo "Add source files under experiments/mini-vla-gridworld/src before running experiments."
    ;;
  *)
    echo "Unknown demo: $demo" >&2
    echo "Available demos: deps-planner-demo, mini-vla-gridworld" >&2
    exit 1
    ;;
esac
