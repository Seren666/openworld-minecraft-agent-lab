#!/usr/bin/env bash
set -u

# Keep normal checks on one GPU by default. Override explicitly only when needed.
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"

if [ -d /root/miniconda3/bin ]; then
  export PATH="/root/miniconda3/bin:${PATH}"
fi

run_section() {
  local title="$1"
  shift

  printf '\n## %s\n\n' "$title"
  printf 'Command: `%s`\n\n' "$*"
  printf '```text\n'
  "$@" 2>&1 || printf '[command failed: %s]\n' "$*"
  printf '```\n'
}

printf '# Remote Environment Audit\n\n'
printf 'Generated at: %s\n\n' "$(date -Iseconds)"
printf 'Default CUDA_VISIBLE_DEVICES: `%s`\n' "${CUDA_VISIBLE_DEVICES}"

run_section "hostname" hostname
run_section "pwd" pwd
run_section "df -h" df -h
run_section "free -h" free -h
run_section "nvidia-smi" nvidia-smi
run_section "nvidia-smi query" nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader
run_section "nvcc --version" bash -lc 'command -v nvcc >/dev/null 2>&1 && nvcc --version || echo "nvcc not found"'
run_section "python --version" bash -lc 'command -v python >/dev/null 2>&1 && python --version || echo "python not found"'
run_section "miniconda python --version" bash -lc '/root/miniconda3/bin/python --version 2>/dev/null || echo "/root/miniconda3/bin/python not found"'
run_section "conda --version" bash -lc 'command -v conda >/dev/null 2>&1 && conda --version || echo "conda not found"'
run_section "git --version" git --version
run_section "echo CUDA_HOME" bash -lc 'printf "%s\n" "${CUDA_HOME:-}"'
run_section "echo PATH" bash -lc 'printf "%s\n" "$PATH"'
