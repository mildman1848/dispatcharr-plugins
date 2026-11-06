# Mildman1848 Dispatcharr plugins

Curated catalog of Dispatcharr plugins maintained by Mildman1848.

## Add as a plugin source

Use this catalog URL when a Dispatcharr plugin source/catalog consumer is configured:

```text
https://raw.githubusercontent.com/mildman1848/dispatcharr-plugins/main/catalog.json
```

The catalog is a discovery document; plugin ZIPs are built by each plugin's GitHub Actions release workflow and attached to tagged GitHub Releases. Do not assume a Dispatcharr version has a native catalog importer—install the ZIP through the method supported by your Dispatcharr version.

## Plugins

| Plugin | Repository | Original projects / references | License |
|---|---|---|---|
| Kodiboxarr | [mildman1848/kodiboxarr](https://github.com/mildman1848/kodiboxarr) | [Kodibox](https://github.com/kodibox32/kodibox), [Dispatcharr](https://github.com/Dispatcharr/Dispatcharr) | AGPL-3.0-only |
| EPGForgearr | [mildman1848/epgforgearr](https://github.com/mildman1848/epgforgearr) | [Dispatcharr](https://github.com/Dispatcharr/Dispatcharr), [EPG reference scripts](https://github.com/michaz1988/michaz1988.github.io/tree/main/.epg) | AGPL-3.0-only |

These are independent community plugins, not endorsed by upstream projects or service providers. See each plugin repository for attribution, provider notes, security guidance, release assets, and source code.

## Catalog format

`catalog.json` follows the schema in [`catalog.schema.json`](catalog.schema.json). Each entry identifies the plugin repository and release download pattern. Release tags use `v<plugin-version>`; each release contains the installable ZIP and `SHA256SUMS`.

## Development and contribution

Each plugin repository runs tests, lint, and a reproducible ZIP build on pushes and pull requests. Use a version bump in `plugin.json`, then push a matching `v<version>` tag to publish an installable ZIP release. Keep generated runtime data, credentials, downloaded provider archives, and signed URLs out of Git.
