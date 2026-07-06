# ROCKET-1 Setup Notes

## Clone

```bash
export CUDA_VISIBLE_DEVICES=0
mkdir -p /root/autodl-tmp/external_repos
cd /root/autodl-tmp/external_repos
git -c http.version=HTTP/1.1 clone https://github.com/CraftJarvis/ROCKET-1.git ROCKET-1
cd ROCKET-1
git remote get-url origin
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD
```

Recorded result:

```text
origin: https://github.com/CraftJarvis/ROCKET-1.git
branch: main
commit: 65cc70e5605a0e0a3b8ec74b52ed399a9b64e321
```

## README Installation Path

The official README describes:

```bash
sudo apt-get install libghc-x11-dev gcc-multilib g++-multilib \
  libglew-dev libosmesa6-dev libgl1-mesa-glx libglfw3

conda create -n rocket python=3.10
conda activate rocket
conda install --channel=conda-forge openjdk=8
pip install -e .

cd rocket/realtime_sam
pip install -e .
cd checkpoints
bash download_ckpts.sh
```

Then it requires downloading `MCP-Reborn.zip` from Hugging Face:

```bash
cd rocket/stark_tech
python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='phython96/ROCKET-MCP-Reborn', filename='MCP-Reborn.zip', local_dir='.')"
unzip MCP-Reborn.zip && rm MCP-Reborn.zip
python env_interface.py
```

## Dependencies Observed

The root `pyproject.toml` declares a broad Minecraft and model stack, including:

```text
opencv-python==4.7.0.72
numpy
lxml
psutil
Pyro4
coloredlogs
pillow
daemoniker
av>=11.0.0
gym / gym3 / gymnasium
hydra-core==1.3.2
transformers==4.31.0
torch
torchvision>=0.16.0
cuda-python
gradio>=5.0.0
openai==1.52.2
```

The `rocket/realtime_sam` package requires `torch>=2.3.1` at build time.

## Checkpoints And Assets

The realtime SAM checkpoint script downloads four Segment Anything 2 checkpoints:

```text
sam2_hiera_tiny.pt
sam2_hiera_small.pt
sam2_hiera_base_plus.pt
sam2_hiera_large.pt
```

These were not downloaded. They are model checkpoints and must not be committed.

The README usage snippet loads ROCKET-1 with:

```python
ROCKET1.from_pretrained("phython96/ROCKET-1").to("cuda")
```

That implies external model weights from Hugging Face. Those weights were not downloaded.

## Safe Checks Run

```bash
cd /root/autodl-tmp/external_repos/ROCKET-1
python -m py_compile rocket/arm/eval_rocket.py rocket/stark_tech/env_interface.py
```

Result:

```text
py_compile_exit: 0
```

No official model inference, simulator rendering, checkpoint download, or training job was started.
