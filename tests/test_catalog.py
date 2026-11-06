from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_entries_reference_public_plugin_repositories():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    assert catalog["registry_name"] == "Mildman1848 Community Plugins"
    assert [plugin["slug"] for plugin in catalog["plugins"]] == ["kodiboxarr", "epgforgearr"]
    assert all(plugin["license"] == "AGPL-3.0-only" for plugin in catalog["plugins"])
    assert all(plugin["repo_url"].startswith("https://github.com/mildman1848/") for plugin in catalog["plugins"])
    assert all(
        "latest_url" not in plugin or plugin["latest_url"].endswith(".zip")
        for plugin in catalog["plugins"]
    )
    kodiboxarr = catalog["plugins"][0]
    assert kodiboxarr["latest_version"] == "0.1.1"
    assert kodiboxarr["latest_url"].endswith("/v0.1.1/kodiboxarr-0.1.1.zip")
    assert len(kodiboxarr["latest_sha256"]) == 64
    epgforgearr = catalog["plugins"][1]
    assert epgforgearr["latest_version"] == "0.3.6-dev"
    assert epgforgearr["latest_url"].endswith("/v0.3.6-dev/epgforgearr-0.3.6-dev.zip")
    assert len(epgforgearr["latest_sha256"]) == 64


def test_catalog_schema_is_valid_json():
    schema = json.loads((ROOT / "catalog.schema.json").read_text(encoding="utf-8"))
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert "registry_name" in schema["required"]
