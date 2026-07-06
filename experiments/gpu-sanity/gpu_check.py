"""Small PyTorch CUDA sanity check.

This script is infrastructure-only. It verifies whether the current PyTorch
installation can execute a tiny tensor workload on CUDA device 0.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_OUTPUT = Path(__file__).resolve().with_name("gpu_check_log.md")


def build_log() -> tuple[str, int]:
    lines = [
        "# GPU Check Log",
        "",
        "This is an infrastructure check, not a research result.",
        "",
    ]

    try:
        import torch
    except Exception as exc:  # pragma: no cover - depends on local environment
        lines.extend(
            [
                "## Result",
                "",
                "PyTorch import failed.",
                "",
                "```text",
                f"{type(exc).__name__}: {exc}",
                "```",
            ]
        )
        return "\n".join(lines) + "\n", 1

    lines.extend(
        [
            "## PyTorch",
            "",
            f"- version: `{torch.__version__}`",
            f"- cuda_available: `{torch.cuda.is_available()}`",
        ]
    )

    if not torch.cuda.is_available():
        lines.extend(["", "## Result", "", "CUDA is not available to PyTorch."])
        return "\n".join(lines) + "\n", 1

    lines.extend(
        [
            f"- device: `{torch.cuda.get_device_name(0)}`",
            f"- arch_list: `{', '.join(torch.cuda.get_arch_list())}`",
            "",
            "## Tensor Workload",
            "",
        ]
    )

    try:
        with torch.no_grad():
            x = torch.randn((256, 256), device="cuda")
            y = (x @ x).sum()
            torch.cuda.synchronize()
            value = float(y.detach().cpu())
        lines.append(f"Tensor workload succeeded. Result checksum: `{value:.6f}`")
        return "\n".join(lines) + "\n", 0
    except Exception as exc:  # pragma: no cover - depends on GPU/PyTorch build
        lines.extend(
            [
                "Tensor workload failed.",
                "",
                "```text",
                f"{type(exc).__name__}: {exc}",
                "```",
            ]
        )
        return "\n".join(lines) + "\n", 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a tiny PyTorch CUDA sanity check.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    log, exit_code = build_log()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(log, encoding="utf-8")
    print(f"wrote {args.output}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
