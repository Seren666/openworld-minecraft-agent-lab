# AutoDL Setup

## Repository Setup

```bash
git clone https://github.com/Seren666/openworld-minecraft-agent-lab.git
cd openworld-minecraft-agent-lab
bash scripts/setup_autodl_env.sh
```

## Storage Rules

- Treat `/root/autodl-tmp` as the primary data disk. The system disk is small and should only hold files that must live there.
- Put external repositories under `/root/autodl-tmp/external_repos`.
- Put optional Conda environments under `/root/autodl-tmp/conda_envs`.
- Put Conda package caches under `/root/autodl-tmp/conda_pkgs`.
- Put pip caches under `/root/autodl-tmp/pip_cache`.
- Put temporary build files under `/root/autodl-tmp/tmp`.
- Put large datasets under `/root/autodl-tmp/datasets`.
- Put checkpoints under `/root/autodl-tmp/checkpoints`, `/root/autodl-tmp/ckpts`, or `/root/autodl-tmp/models`.
- Put generated outputs under `/root/autodl-tmp/outputs`, `/root/autodl-tmp/runs`, or `/root/autodl-tmp/logs`.
- Keep small Markdown summaries in `experiments/`.
- Do not commit the data-disk directories above to GitHub.

Recommended environment variables before installs:

```bash
export CUDA_VISIBLE_DEVICES=0
export CONDA_PKGS_DIRS=/root/autodl-tmp/conda_pkgs
export PIP_CACHE_DIR=/root/autodl-tmp/pip_cache
export TMPDIR=/root/autodl-tmp/tmp
mkdir -p /root/autodl-tmp/{external_repos,conda_envs,conda_pkgs,pip_cache,tmp,datasets,checkpoints,outputs,runs,logs}
```

## Run Log Template

```text
Date:
Machine:
GPU:
Python:
Command:
Result:
Issue:
Fix:
```
