from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_entries_reference_public_plugin_repositories():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    assert catalog["schema_version"] == 1
    assert [plugin["id"] for plugin in catalog["plugins"]] == [
        "mildman1848.kodiboxarr",
        "mildman1848.epgforgearr",
    ]
    assert all(plugin["license"] == "AGPL-3.0-only" for plugin in catalog["plugins"])
    assert all(plugin["repository"].startswith("https://github.com/mildman1848/") for plugin in catalog["plugins"])
    assert all(plugin["release"]["checksum_asset"] == "SHA256SUMS" for plugin in catalog["plugins"])


def test_catalog_schema_is_valid_json():
    schema = json.loads((ROOT / "catalog.schema.json").read_text(encoding="utf-8"))
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["properties"]["schema_version"]["const"] == 1
