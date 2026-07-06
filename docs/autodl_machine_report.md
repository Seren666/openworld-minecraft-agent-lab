# AutoDL Machine Report

Audited on 2026-07-06 for the Open-World Minecraft Agent Lab repository.

This report intentionally omits the SSH endpoint, password, raw hostname, private mount host address, and full `PATH`. Do not commit secrets, access details, private machine identifiers, model weights, datasets, checkpoints, raw videos, or large output files.

## Repository Sync

Target repository path:

```text
/root/autodl-tmp/openworld-minecraft-agent-lab
```

Result:

```text
git clone https://github.com/Seren666/openworld-minecraft-agent-lab.git /root/autodl-tmp/openworld-minecraft-agent-lab
git status --short --branch
## main...origin/main
```

Large local-only working directories were created outside the Git repository:

```text
/root/autodl-tmp/external_repos
/root/autodl-tmp/datasets
/root/autodl-tmp/checkpoints
/root/autodl-tmp/outputs
/root/autodl-tmp/logs
```

## Audit Commands

The following commands were run during the initial audit. Sensitive raw values are summarized or redacted.

| Command | Result |
| --- | --- |
| `hostname` | Ran successfully. Raw hostname redacted from committed report. |
| `pwd` | `/root/autodl-tmp/openworld-minecraft-agent-lab` |
| `df -h` | Root overlay: 30G total, about 30G available. Public/shared storage mounted at `/autodl-pub`: 7.3T total, 5.3T available. Shared memory: 360G. Private backing host address omitted. |
| `free -h` | 1.0Ti total RAM, about 988Gi available, no swap. |
| `nvidia-smi` | 6 GPUs visible, no running GPU processes during audit. |
| `nvcc --version` | CUDA compilation tools release 11.8, V11.8.89. |
| `python --version` | `python` was not found in the non-login shell PATH. `/root/miniconda3/bin/python --version` reports Python 3.10.8. |
| `conda --version` | Conda 22.11.1 available under `/root/miniconda3/bin/conda`. |
| `git --version` | Git 2.34.1. |
| `echo $CUDA_HOME` | Empty / unset during audit. |
| `echo $PATH` | Ran successfully. Full value omitted; relevant entries include Miniconda, NVIDIA, CUDA, and system binary directories. |

## GPU Summary

| Item | Value |
| --- | --- |
| GPU count | 6 |
| GPU model | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| Memory per GPU | 97,887 MiB |
| Driver version | 595.71.05 |
| CUDA reported by `nvidia-smi` | 13.2 |
| CUDA toolkit reported by `nvcc` | 11.8 |
| Default GPU policy | Use one GPU by default with `CUDA_VISIBLE_DEVICES=0`. |

## CPU and RAM Summary

| Item | Value |
| --- | --- |
| CPU model | Intel Xeon Platinum 8470Q |
| Logical CPUs | 208 |
| Sockets | 2 |
| Cores per socket | 52 |
| Threads per core | 2 |
| RAM | 1.0Ti total, about 988Gi available during audit |
| Swap | 0B |

## Disk Layout Summary

| Location | Purpose | Notes |
| --- | --- | --- |
| `/root/autodl-tmp/openworld-minecraft-agent-lab` | Clean Git working copy | Safe files only. |
| `/root/autodl-tmp/external_repos` | Third-party repositories | Local only; do not commit. |
| `/root/autodl-tmp/datasets` | Datasets | Local only; do not commit. |
| `/root/autodl-tmp/checkpoints` | Model checkpoints | Local only; do not commit. |
| `/root/autodl-tmp/outputs` | Generated experiment outputs | Local only; summarize before committing. |
| `/root/autodl-tmp/logs` | Raw run logs | Local only; commit only small summarized Markdown logs. |
| `/autodl-pub` | Shared/public storage mount | Backing host address omitted from committed docs. |

## Recommended Use for This Project

- Use this machine for environment setup, MineStudio checks, small planner demos, and later GPU-heavy experiments.
- Start every normal test with `CUDA_VISIBLE_DEVICES=0` unless a task explicitly needs more GPUs.
- Prefer `/root/miniconda3/bin/python` or an explicitly activated Conda environment when running scripts over SSH.
- Keep raw datasets, checkpoints, model weights, generated videos, and large outputs under `/root/autodl-tmp`.
- Commit only notes, small configs, scripts, summarized Markdown logs, and small screenshots.
- Before every push, run `git status --short`, inspect staged files, and check for secrets or large artifacts.

## Safety Warning

Large files and private machine information must not be committed. In particular, do not commit SSH configuration, tokens, passwords, IP addresses, raw hostnames, private mount addresses, datasets, checkpoints, model weights, raw videos, or large experiment outputs.
