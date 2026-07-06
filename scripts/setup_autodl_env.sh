#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

if [[ -f requirements.txt ]]; then
  python -m pip install -r requirements.txt
else
  echo "No requirements.txt found. Add one when an experiment needs pinned packages."
fi

echo "AutoDL-style Python environment is ready."
