#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/architecture/PLATFORM_TREE.md"
EXCLUDED_FILE = "scripts/.rebuild_stats.json"


def render(base: Path, rel: Path = Path("."), prefix: str = "") -> list[str]:
    def include_path(p: Path) -> bool:
        relp = p.relative_to(ROOT).as_posix()
        if relp == ".git" or relp.startswith(".git/"):
            return False
        if relp == EXCLUDED_FILE:
            return False
        if p.is_file() and p.name.endswith(".stats.json"):
            return False
        return True

    children = [p for p in (base / rel).iterdir() if include_path(p)]
    children.sort(key=lambda p: (p.is_file(), p.name.lower()))
    lines: list[str] = []
    for idx, child in enumerate(children):
        is_last = idx == len(children) - 1
        connector = "└─ " if is_last else "├─ "
        lines.append(prefix + connector + child.name + ("/" if child.is_dir() else ""))
        if child.is_dir():
            child_prefix = prefix + ("   " if is_last else "│  ")
            lines.extend(render(base, rel / child.name, child_prefix))
    return lines


def main() -> int:
    lines = ["bizplatform/"] + render(ROOT)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "# bizplatform canonical repository tree\n\n```text\n"
        + "\n".join(lines)
        + "\n```\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
