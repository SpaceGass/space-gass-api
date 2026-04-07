# CLAUDE.md

Project context and decisions for the `space-gass-api` repository.

## Overview

This is the public developer-facing repo for the SPACE GASS API. It contains the OpenAPI spec, auto-generated Kiota SDKs, hand-crafted examples, and a Zudoku documentation site deployed to GitHub Pages.

## Key Decisions

### Branching

- **Default branch:** `develop` (not `main`)
- All CI workflows trigger on `develop`

### Licensing

- **MIT** — SDKs, examples, sandbox (`sdks/`, `sandbox/`)
- **CC BY-ND 4.0** — OpenAPI specifications (`descriptions/`)
- `LICENSE` at root covers MIT; `LICENSE-SPEC` covers CC BY-ND
- `descriptions/NOTICE.md` explains the boundary to developers

### OpenAPI Spec Naming

- Use **generic filenames** in `preview/` and `current/`: `openapi.json`
- Use **versioned filenames** in `archive/`: `openapi-v14.5.0.json`
- The version is embedded inside the spec file itself — the filename doesn't need to carry it in folders where configs need a stable path
- No product name in the filename (repo name already provides context)

### SDK Client Naming

| Context | Convention | Value |
|---|---|---|
| Kiota C# namespace | PascalCase | `SpaceGassApi` |
| Kiota Python namespace | snake_case | `space_gass_api` |
| NuGet package ID | PascalCase | `SpaceGassApi` |
| PyPI package name | kebab-case | `space-gass-api` |
| C# using statements | `SpaceGassApi` / `SpaceGassApi.Models` | (not `SpaceGassApi.Client`) |
| Python imports | `space_gass_api` | (not `spacegass_client`) |

### SDK Generation (Kiota)

- Clients in `sdks/*/client/` are **auto-generated** — never hand-edit
- `kiota.config.json` at the root defines both C# and Python targets
- Both point to `descriptions/preview/openapi.json` (stable path)
- The `generate-clients` workflow is **manual trigger** (`workflow_dispatch`)

### Examples

- **C# examples** use `ProjectReference` to `../../client/SpaceGassApi/SpaceGassApi.csproj` (will switch to NuGet package reference once published)
- **Python examples** are organized in individual **snake_case folders** (`create_simple_beam/`, `run_analysis/`, etc.)
- Shared helper `client_factory.py` stays at the Python examples root
- C# examples follow `Example.PascalCase` folder naming with a shared `SpaceGassApi.Examples.Common` library

### Documentation Site (Zudoku)

- Built with [Zudoku](https://zudoku.dev) v0.69.3
- **`basePath: "/space-gass-api"`** is required in `zudoku.config.tsx` for GitHub Pages asset paths
- The deploy workflow uploads `docs/dist/space-gass-api` (the inner basePath directory) as the Pages artifact to avoid double-nesting
- A postinstall patch (`docs/patches/fix-zudoku-mjs.js`) fixes a Vite 7 SSR `.mjs` issue
- The API reference reads from `../descriptions/preview/openapi.json` (single source of truth)
- `node_modules/` is never committed — `npm ci` regenerates it

### GitHub Pages Deployment

- Source: **GitHub Actions** (not "Deploy from a branch")
- URL: `https://spacegass.github.io/space-gass-api/`
- Workflow: `.github/workflows/deploy-docs.yml`
- Uses `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true` to suppress Node 20 deprecation warnings

### CI/CD Workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| `deploy-docs.yml` | Push to `develop` | Build Zudoku site and deploy to GitHub Pages |
| `generate-clients.yml` | Manual (`workflow_dispatch`) | Run Kiota to regenerate SDK clients |
| `publish-packages.yml` | GitHub Release published | Publish to NuGet and PyPI |

### Versioning

- SDK versions mirror the SPACE GASS Desktop version (e.g., Desktop v15.0.2 = NuGet `SpaceGassApi 15.0.2`)
- The `descriptions/current/` folder won't exist until the first formal release
- The repo starts in **preview state** with specs in `descriptions/preview/`
