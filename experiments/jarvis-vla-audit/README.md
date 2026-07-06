# JARVIS-VLA Audit

This folder records a bounded JARVIS-VLA paper and repository audit. It is not an official end-to-end reproduction, not a training run, and not a claim of official Minecraft task success.

## Goal

Understand how JARVIS-VLA adapts vision-language models toward action prediction in Minecraft-like visual games, then identify a small safe artifact for research email outreach.

## Upstream Sources

| Item | Value |
| --- | --- |
| Paper title | `JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse` |
| Paper | `https://arxiv.org/abs/2503.16365` |
| Project page | `https://craftjarvis.github.io/JarvisVLA/` |
| Official repository | `https://github.com/CraftJarvis/JarvisVLA.git` |
| Models collection | `https://huggingface.co/collections/CraftJarvis/jarvis-vla-v1-67dc157a99d011efd7d7f7e4` |
| Dataset page | `https://huggingface.co/datasets/CraftJarvis/minecraft-vla-sft` |

## Repository Snapshot

| Item | Value |
| --- | --- |
| External path | `/root/autodl-tmp/external_repos/JarvisVLA` |
| Branch | `master` |
| Commit | `0aafd2ed0ba9270f40d710440ca70cdc3fa48a11` |
| Last commit summary | `0aafd2e 2025-08-27 14:50:15 +0000 add craft&smelt agent&fix sample bugs` |

External code, model weights, datasets, raw videos, and large logs stay outside this GitHub repository.

## Storage Policy On AutoDL

The AutoDL system disk is small. During this audit, external repos, caches, temp files, logs, and optional environments were kept on the data disk:

```text
/root/autodl-tmp/external_repos
/root/autodl-tmp/conda_envs
/root/autodl-tmp/conda_pkgs
/root/autodl-tmp/pip_cache
/root/autodl-tmp/tmp
/root/autodl-tmp/logs
```

## Local Demo

The paired toy action-interface demo lives in:

```text
experiments/jarvis-vla-action-demo/
```

It is rule-based and optional-GPU-scored. It illustrates the action-interface idea without official JARVIS-VLA checkpoints.
