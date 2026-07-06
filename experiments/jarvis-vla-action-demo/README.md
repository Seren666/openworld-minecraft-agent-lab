# JARVIS-VLA Action Demo

This folder contains a lightweight VLA action-interface demo inspired by JARVIS-VLA. It is not a trained model and not an official reproduction.

## Idea

JARVIS-VLA studies how vision-language models can be post-trained toward action prediction in visual games. The key interface is:

```text
vision-language input + task instruction + action space -> structured game action
```

This demo uses toy Minecraft-like observations and a small discrete action space to show how action prediction differs from high-level planning.

## Files

| File | Purpose |
| --- | --- |
| `action_space.json` | Small toy action schema |
| `demo_scenes.json` | Toy Minecraft-like scenes |
| `vla_action_demo.py` | Rule-based action-interface demo |
| `gpu_action_scorer.py` | Optional tiny GPU-backed action scorer |
| `logs/example_run.md` | Generated rule-based run log |
| `logs/gpu_action_scorer_log.md` | Generated GPU scorer log when run on AutoDL |

## Run

From the repository root:

```bash
python experiments/jarvis-vla-action-demo/vla_action_demo.py
```

On AutoDL, using the data-disk Blackwell PyTorch environment:

```bash
CUDA_VISIBLE_DEVICES=0 \
  /root/autodl-tmp/conda_envs/blackwell-torch-test/bin/python \
  experiments/jarvis-vla-action-demo/gpu_action_scorer.py
```

## Limitations

- No official JARVIS-VLA checkpoint is used.
- No MineStudio simulator is launched.
- No model is trained.
- The rule-based selector and tiny GPU scorer are explanatory artifacts only.
