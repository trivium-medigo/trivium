#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/architecture/platform_tree_manifest.json"
TREE_MD = ROOT / "docs/architecture/PLATFORM_TREE.md"
EXCLUDED_FILE = "scripts/.rebuild_stats.json"


def norm(p: str) -> str:
    return p.replace("\\", "/").strip("/")


def _is_js_tooling_artifact(rel: str) -> bool:
    """Installed dependency trees and local task caches are not manifest inventory; committed lockfiles are."""
    parts = rel.split("/")
    if "node_modules" in parts:
        return True
    if rel == ".turbo" or rel.startswith(".turbo/"):
        return True
    return False


def build_physical_index() -> tuple[set[str], set[str]]:
    dirs: set[str] = set()
    files: set[str] = set()
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT).as_posix()
        if rel == ".git" or rel.startswith(".git/"):
            continue
        if _is_js_tooling_artifact(rel):
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


def load_manifest() -> tuple[set[str], set[str]]:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    files = {norm(p) for p in data.get("files", [])}
    files = {p for p in files if p != EXCLUDED_FILE and not p.endswith(".stats.json")}
    return (
        {norm(p) for p in data.get("directories", [])},
        files,
    )


def main() -> int:
    errors: list[str] = []

    if not MANIFEST.exists():
        errors.append("missing manifest: docs/architecture/platform_tree_manifest.json")
        print("INVALID")
        for e in errors:
            print(e)
        return 1

    physical_dirs, physical_files = build_physical_index()
    expected_dirs, expected_files = load_manifest()

    missing_dirs = sorted(expected_dirs - physical_dirs)
    missing_files = sorted(expected_files - physical_files)
    extra_dirs = sorted(physical_dirs - expected_dirs)
    extra_files = sorted(physical_files - expected_files)

    if missing_dirs:
        errors.append(f"manifest missing dirs ({len(missing_dirs)})")
    if missing_files:
        errors.append(f"manifest missing files ({len(missing_files)})")
    if extra_dirs:
        errors.append(f"manifest extra dirs ({len(extra_dirs)})")
    if extra_files:
        errors.append(f"manifest extra files ({len(extra_files)})")

    # Hard rules
    if (ROOT / "bizplatform").exists():
        errors.append("nested bizplatform/ folder exists")
    if not (ROOT / ".git").exists():
        errors.append(".git/ does not exist")
    if TREE_MD.exists() and ".git/" in TREE_MD.read_text(encoding="utf-8", errors="ignore"):
        errors.append(".git/ appears in PLATFORM_TREE.md")

    siblings = ["apps/api", "apps/web", "apps/mobile", "apps/desktop", "apps/portals", "apps/bff"]
    for s in siblings:
        p = ROOT / s
        if not p.exists() or p.parent != ROOT / "apps":
            errors.append(f"sibling missing/invalid: {s}")

    if not (ROOT / "apps/web/app/(public)/app-entry/page.tsx").exists():
        errors.append("missing apps/web/app/(public)/app-entry/page.tsx")
    if (ROOT / "apps/web/app/(public)/login/page.tsx").exists():
        errors.append("forbidden apps/web/app/(public)/login/page.tsx exists")
    if not (ROOT / "docs/providers/regional-banks/russia/disabled-legal-review.md").exists():
        errors.append("missing docs/providers/regional-banks/russia/disabled-legal-review.md")

    forbidden_prefixes = [
        "docs/providers/bank-feeds-global",
        "docs/providers/hr",
        "security/threat-model",
        "workers/wise-bank-feed-worker",
        "workers/export-expiry-worker",
        "workers/outbound-dry-run-worker",
    ]
    for prefix in forbidden_prefixes:
        if (ROOT / prefix).exists():
            errors.append(f"forbidden alias exists: {prefix}")

    flat_alias_re = re.compile(
        r"^docs/providers/regional-banks/(?:mk|rs|me|hr|bg|gr|tr|pl|ca|mx|in|apac)-[^/]+\.md$"
    )
    for f in physical_files:
        if flat_alias_re.match(f):
            errors.append(f"forbidden flat regional alias exists: {f}")

    must_exist = [
        "warehouse",
        "search",
        "vector-store",
        "databases/warehouse",
        "databases/search",
        "databases/vector-store",
        "services/integrations-platform-service",
        "services/integrations-orchestration-service",
        "services/search-service",
        "services/search-index-service",
        "workers/bank-feed-wise-worker",
        "workers/bank-feed-mercury-worker",
        "workers/bank-feed-plaid-worker",
        "workers/bank-feed-gocardless-worker",
        "workers/bank-feed-truelayer-worker",
        "workers/bank-feed-teller-worker",
        "workers/bank-feed-stripe-financial-connections-worker",
        "workers/bank-feed-stripe-treasury-worker",
        "platform/environment-management",
        "platform/runtime/environment-management",
    ]
    for p in must_exist:
        if not (ROOT / p).exists():
            errors.append(f"missing canonical kept path: {p}")

    if errors:
        print("INVALID")
        for e in errors:
            print(e)
        if missing_dirs:
            print("sample_missing_dir:", missing_dirs[0])
        if missing_files:
            print("sample_missing_file:", missing_files[0])
        if extra_dirs:
            print("sample_extra_dir:", extra_dirs[0])
        if extra_files:
            print("sample_extra_file:", extra_files[0])
        return 1

    print("VALID")
    print(f"manifest_dirs={len(expected_dirs)} manifest_files={len(expected_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
