# DEPS / MC-Planner Run Log

This is a summarized run log for a lightweight DEPS-style reproduction. It is not a complete official reproduction.

## 2026-07-06 AutoDL Setup Pass

### Goal

Inspect the official or most relevant DEPS / MC-Planner implementation, attempt bounded setup, and create a planning-only demonstration suitable for a research email.

### Upstream Repository

| Item | Value |
| --- | --- |
| Repository | `https://github.com/CraftJarvis/MC-Planner.git` |
| Branch | `main` |
| Commit | `2a8b5a3e453c39634c2674d03e5ac21605270939` |
| External path | `/root/autodl-tmp/external_repos/MC-Planner` |

### Commands and Results

| Command | Result |
| --- | --- |
| `git clone https://github.com/CraftJarvis/MC-Planner.git /root/autodl-tmp/external_repos/MC-Planner` | Failed on AutoDL with GitHub transport errors: HTTP/2 framing error, then HTTPS timeout. |
| Download GitHub `main` source archive | Succeeded locally; archive unpacked under `/root/autodl-tmp/external_repos/MC-Planner` for inspection. |
| Inspect `README.md` | Succeeded. README identifies Python >= 3.9, `requirements.txt`, MineCLIP, modified MineDojo / MC-Simulator, controller checkpoint, and OpenAI keys. |
| Inspect `requirements.txt` | Succeeded. Key dependencies include `ray[rllib]`, `gym`, `gym3`, `hydra-core`, `transformers`, `wandb`, `openai==0.23.0`, and a README-specified PyTorch nightly wheel. |
| `conda create -n mc-planner-test python=3.10` | Succeeded. |
| Official `python main.py model.load_ckpt_path=<path/to/ckpt>` | Not run. Required controller checkpoint, modified simulator, OpenAI keys, and Minecraft rendering environment were not prepared in this bounded pass. |

### Official Setup Requirements Observed

- Python >= 3.9
- PyTorch nightly `torch==2.0.0.dev20230208+cu117` in the README
- `requirements.txt`
- `git+https://github.com/MineDojo/MineCLIP`
- Modified MineDojo simulator from `https://github.com/CraftJarvis/MC-Simulator`
- Goal-conditioned controller checkpoint from an external download link
- OpenAI keys in `data/openai_keys.txt`
- Minecraft simulator window for full agent execution

### Planning-Only Demo Result

Because the official run depends on external keys, checkpoints, simulator setup, and Minecraft rendering, this pass created a local planning-only record for:

1. Obtain wooden pickaxe
2. Craft stone sword
3. Obtain iron ingot
4. Build a small shelter

The examples are in `task_examples.md`.

### Blockers

- AutoDL GitHub clone of MC-Planner failed due transport/network issues.
- OpenAI API key file is required for the official planner.
- Controller checkpoint was not downloaded.
- Modified MineDojo / MC-Simulator was not installed.
- Full execution would require Minecraft simulator setup and rendering support.

### What Worked

- Official repository and commit were identified.
- Source archive was inspected outside this repository.
- Python 3.10 Conda environment creation succeeded.
- The project structure, dependencies, and official run path were documented.
- A lightweight DEPS-style planning record was created without external keys or large assets.

### What Failed Or Was Deferred

- True `git clone` on AutoDL failed for MC-Planner.
- Full dependency installation was deferred because it would pull simulator/controller/model components beyond this short email-prep pass.
- No Minecraft environment was launched.
- No controller checkpoint was loaded.

### Next Step

If a deeper reproduction is needed, prepare OpenAI-compatible planning access, MC-Simulator, MineCLIP, and the controller checkpoint in `/root/autodl-tmp`, then run one official task with a short timeout and no large committed outputs.
