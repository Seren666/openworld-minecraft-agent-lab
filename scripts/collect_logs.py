"""Collect small text logs into a single Markdown digest."""

from __future__ import annotations

import argparse
from pathlib import Path


TEXT_SUFFIXES = {".md", ".txt", ".log"}


def iter_log_files(source: Path) -> list[Path]:
    return sorted(
        path
        for path in source.rglob("*")
        if path.is_file()
        and path.suffix.lower() in TEXT_SUFFIXES
        and ".git" not in path.parts
    )


def read_small_text(path: Path, max_bytes: int) -> str | None:
    if path.stat().st_size > max_bytes:
        return None
    return path.read_text(encoding="utf-8", errors="replace").strip()


def build_digest(source: Path, max_bytes: int) -> str:
    sections = ["# Collected Experiment Logs", ""]
    for path in iter_log_files(source):
        content = read_small_text(path, max_bytes=max_bytes)
        if not content:
            continue
        sections.extend(
            [
                f"## {path.as_posix()}",
                "",
                "```text",
                content,
                "```",
                "",
            ]
        )
    return "\n".join(sections).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("experiments"))
    parser.add_argument("--output", type=Path, default=Path("docs/collected_logs.md"))
    parser.add_argument("--max-bytes", type=int, default=32_000)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        build_digest(args.source, max_bytes=args.max_bytes),
        encoding="utf-8",
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
