#!/usr/bin/env python3
"""Update the EPGForgearr entry from a verified GitHub release asset."""

import argparse
import json
import re
from pathlib import Path


def update_catalog(path: Path, version: str, asset_url: str, sha256: str) -> bool:
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("version must be a stable semantic version")
    if not re.fullmatch(r"[0-9a-f]{64}", sha256):
        raise ValueError("sha256 must be 64 lowercase hexadecimal characters")
    expected_url = f"https://github.com/mildman1848/epgforgearr/releases/download/v{version}/epgforgearr-{version}.zip"
    if asset_url != expected_url:
        raise ValueError("release asset URL does not match the expected EPGForgearr release asset")

    catalog = json.loads(path.read_text(encoding="utf-8"))
    matches = [item for item in catalog["plugins"] if item.get("slug") == "epgforgearr"]
    if len(matches) != 1:
        raise ValueError("catalog must contain exactly one EPGForgearr entry")
    entry = matches[0]
    new_values = {"latest_version": version, "latest_url": asset_url, "latest_sha256": sha256}
    if all(entry.get(key) == value for key, value in new_values.items()):
        return False
    entry.update(new_values)
    path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--sha256", required=True)
    parser.add_argument("--catalog", type=Path, default=Path("catalog.json"))
    args = parser.parse_args()
    changed = update_catalog(args.catalog, args.version, args.url, args.sha256)
    print("updated" if changed else "already current")


if __name__ == "__main__":
    main()
