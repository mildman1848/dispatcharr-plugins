from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from update_epgforgearr_catalog import update_catalog  # noqa: E402


def test_update_catalog_updates_only_epgforgearr_and_is_idempotent(tmp_path):
    path = tmp_path / "catalog.json"
    path.write_text(json.dumps({"plugins": [
        {"slug": "keep", "latest_version": "1.0.0"},
        {"slug": "epgforgearr", "latest_version": "0.3.9"},
    ]}), encoding="utf-8")
    url = "https://github.com/mildman1848/epgforgearr/releases/download/v0.4.0/epgforgearr-0.4.0.zip"
    digest = "a" * 64

    assert update_catalog(path, "0.4.0", url, digest)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["plugins"][0] == {"slug": "keep", "latest_version": "1.0.0"}
    assert data["plugins"][1] == {"slug": "epgforgearr", "latest_version": "0.4.0", "latest_url": url, "latest_sha256": digest}
    assert not update_catalog(path, "0.4.0", url, digest)


def test_update_catalog_rejects_invalid_hash_and_url(tmp_path):
    path = tmp_path / "catalog.json"
    path.write_text('{"plugins": [{"slug": "epgforgearr"}]}', encoding="utf-8")
    with pytest.raises(ValueError, match="sha256"):
        update_catalog(path, "0.4.0", "https://example.invalid/asset.zip", "bad")
    with pytest.raises(ValueError, match="URL"):
        update_catalog(path, "0.4.0", "https://example.invalid/asset.zip", "a" * 64)


def test_update_catalog_requires_one_entry(tmp_path):
    path = tmp_path / "catalog.json"
    path.write_text('{"plugins": []}', encoding="utf-8")
    with pytest.raises(ValueError, match="exactly one"):
        update_catalog(path, "0.4.0", "https://github.com/mildman1848/epgforgearr/releases/download/v0.4.0/epgforgearr-0.4.0.zip", "a" * 64)
