# SPACE GASS API

Official SPACE GASS API specifications, developer SDKs, and automation examples.

## Overview

This repository is the public home of the SPACE GASS API ecosystem. It contains:

- **OpenAPI Specifications** — the canonical API definition used to generate SDKs and documentation
- **SDKs** — auto-generated client libraries for C# and Python, published to NuGet and PyPI
- **Examples** — hand-crafted code samples demonstrating common workflows
- **Documentation** — the developer docs site, powered by [Zudoku](https://zudoku.dev)

> **Developer docs:** [https://spacegass.github.io/space-gass-api/](https://spacegass.github.io/space-gass-api/)

## Quick Start

### C# (.NET)

```bash
dotnet add package SpaceGassApi
```

### Python

```bash
pip install space-gass-api
```

See the [Getting Started](https://spacegass.github.io/space-gass-api/) guides for detailed setup instructions.

## Repository Structure

```
space-gass-api/
├── descriptions/       # OpenAPI specifications (CC BY-ND 4.0)
│   ├── current/        # Latest released spec
│   ├── preview/        # Pre-release spec (subject to breaking changes)
│   └── archive/        # Previous versions
├── sdks/
│   ├── csharp/
│   │   ├── client/     # Auto-generated Kiota client (do not hand-edit)
│   │   └── examples/   # Hand-crafted C# examples
│   └── python/
│       ├── client/     # Auto-generated Kiota client (do not hand-edit)
│       └── examples/   # Hand-crafted Python examples
├── sandbox/            # Informal scripts and experiments
└── docs/               # Developer documentation site (Zudoku)
```

## Versioning

SDK and package versions mirror the SPACE GASS Desktop version. For example, SPACE GASS Desktop v15.0.2 corresponds to `SpaceGassApi 15.0.2` on NuGet and `space-gass-api==15.0.2` on PyPI.

## Licensing

This repository uses a dual-license strategy:

| Content | License |
|---|---|
| SDKs, examples, and sandbox scripts | [MIT](LICENSE) |
| OpenAPI specifications (`descriptions/`) | [CC BY-ND 4.0](LICENSE-SPEC) |

The MIT license gives you full freedom to use, modify, and distribute the SDK code. The CC BY-ND license protects the integrity of the API specification while still allowing you to use it freely.

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved.
