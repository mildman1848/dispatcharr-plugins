# Mildman1848 Dispatcharr plugins

Curated catalog of Dispatcharr plugins maintained by Mildman1848.

## Add as a plugin source

Add this manifest URL under Dispatcharr's **Manage Repos / Add Repository**:

```text
https://raw.githubusercontent.com/mildman1848/dispatcharr-plugins/main/catalog.json
```

This is a Dispatcharr repository manifest (`registry_name` + `plugins`), not a custom catalog schema. Plugin ZIPs are built by each plugin's GitHub Actions release workflow and attached to tagged GitHub Releases.

## Plugins

| Plugin | Repository | Original projects / references | License |
|---|---|---|---|
| Kodiboxarr | [mildman1848/kodiboxarr](https://github.com/mildman1848/kodiboxarr) | [Kodibox](https://github.com/kodibox32/kodibox), [Dispatcharr](https://github.com/Dispatcharr/Dispatcharr) | AGPL-3.0-only |
| EPGForgearr | [mildman1848/epgforgearr](https://github.com/mildman1848/epgforgearr) | [Dispatcharr](https://github.com/Dispatcharr/Dispatcharr), [EPG reference scripts](https://github.com/michaz1988/michaz1988.github.io/tree/main/.epg) | AGPL-3.0-only |

These are independent community plugins, not endorsed by upstream projects or service providers. See each plugin repository for attribution, provider notes, security guidance, release assets, and source code.

## Catalog format

`catalog.json` follows Dispatcharr's [plugin repository manifest specification](https://github.com/Dispatcharr/Dispatcharr/blob/main/Plugin_repo.md) and the local schema in [`catalog.schema.json`](catalog.schema.json). Release downloads are version-pinned GitHub Release ZIP URLs.

## Development and contribution

Each plugin repository runs tests, lint, and a reproducible ZIP build on pushes and pull requests. Use a version bump in `plugin.json`, then push a matching `v<version>` tag to publish an installable ZIP release. Keep generated runtime data, credentials, downloaded provider archives, and signed URLs out of Git.
