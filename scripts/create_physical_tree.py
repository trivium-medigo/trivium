#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/architecture/platform_tree_manifest.json"
EXCLUDED_FILE = "scripts/.rebuild_stats.json"


def placeholder_content(path: Path) -> str:
    if path.name == "README.md":
        return f"# {path.parent.name or 'root'}\n\nPlaceholder.\n"
    if path.suffix == ".md":
        return f"# {path.stem}\n\nPlaceholder.\n"
    if path.suffix == ".ts":
        return "export {};\n"
    if path.suffix == ".tsx":
        return "export default function Placeholder() { return null; }\n"
    if path.suffix == ".json":
        return "{}\n"
    if path.suffix in {".yaml", ".yml"}:
        return "{}\n"
    if path.suffix == ".sql":
        return "-- placeholder\n"
    if path.name == "Dockerfile":
        return "# placeholder\n"
    if path.suffix == ".py":
        return "#!/usr/bin/env python3\n\nif __name__ == '__main__':\n    print('placeholder')\n"
    return "placeholder\n"


def load_manifest() -> dict:
    if not MANIFEST.exists():
        raise FileNotFoundError(f"Manifest not found: {MANIFEST}")
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def normalize(path: str) -> str:
    return path.replace("\\", "/").strip("/")


def build_physical_index() -> tuple[set[str], set[str]]:
    dirs: set[str] = set()
    files: set[str] = set()
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT).as_posix()
        if rel == ".git" or rel.startswith(".git/"):
            continue
        if "node_modules" in rel.split("/"):
            continue
        if rel == ".turbo" or rel.startswith(".turbo/"):
            continue
        if rel == EXCLUDED_FILE:
            continue
        if p.is_file() and p.name.endswith(".stats.json"):
            continue
        if p.is_dir():
            dirs.add(rel)
        else:
            files.add(rel)
    return dirs, files


def main() -> int:
    parser = argparse.ArgumentParser(description="Create missing tree paths from manifest.")
    parser.add_argument(
        "--delete-extra",
        action="store_true",
        help="Delete filesystem paths not present in manifest (excluding .git).",
    )
    args = parser.parse_args()

    manifest = load_manifest()
    expected_dirs = {normalize(p) for p in manifest.get("directories", [])}
    expected_files = {normalize(p) for p in manifest.get("files", [])}
    expected_files = {p for p in expected_files if p != EXCLUDED_FILE and not p.endswith(".stats.json")}

    created_dirs = 0
    created_files = 0
    deleted_paths = 0

    for d in sorted(expected_dirs):
        target = ROOT / d
        if not target.exists():
            target.mkdir(parents=True, exist_ok=True)
            created_dirs += 1

    for f in sorted(expected_files):
        target = ROOT / f
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(placeholder_content(target), encoding="utf-8")
            created_files += 1

    if args.delete_extra:
        physical_dirs, physical_files = build_physical_index()
        extra_files = sorted(physical_files - expected_files)
        extra_dirs = sorted(physical_dirs - expected_dirs, key=lambda x: len(x.split("/")), reverse=True)

        for rel in extra_files:
            target = ROOT / rel
            if target.exists():
                target.unlink()
                deleted_paths += 1
        for rel in extra_dirs:
            target = ROOT / rel
            if target.exists() and target.is_dir():
                try:
                    target.rmdir()
                    deleted_paths += 1
                except OSError:
                    pass

    print(
        f"create_physical_tree: created_dirs={created_dirs} created_files={created_files} "
        f"deleted_paths={deleted_paths} delete_extra={args.delete_extra}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
