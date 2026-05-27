# CLAUDE.md

Project context and decisions for the `space-gass-api` repository.

## Overview

This is the public developer-facing repo for the SPACE GASS API. It contains the OpenAPI spec, auto-generated Kiota SDKs, hand-crafted examples, and a Zudoku documentation site deployed to GitHub Pages.

## Key Decisions

### Branching

- **Default branch:** `main`
- All CI workflows trigger on `main`

### Licensing

- **MIT** — SDKs, examples, sandbox (`sdks/`, `sandbox/`)
- **SPACE GASS License** — OpenAPI specifications (`descriptions/`)
- `LICENSE` at root covers MIT; OpenAPI specs are subject to the [SPACE GASS EULA](https://www.spacegass.com/manual/Introduction/End_User_Licence_Agreement.htm)
- `descriptions/NOTICE.md` explains the boundary to developers

### OpenAPI Spec Naming

- Use **`SpaceGassApi.json`** in `preview/` and `current/` — matches the project output name
- Use **versioned filenames** in `archive/`: `openapi-v14.5.0.json`
- The version is embedded inside the spec file itself — the filename doesn't need to carry it in folders where configs need a stable path

### SDK Client Naming

| Context | Convention | Value |
|---|---|---|
| Kiota C# namespace | PascalCase | `SpaceGassApi` |
| Kiota Python namespace | snake_case | `space_gass_api.generated` |
| NuGet package ID | PascalCase | `SpaceGassApi` |
| PyPI package name | kebab-case | `space-gass-api` |
| C# using statements | `SpaceGassApi` / `SpaceGassApi.Models` | (not `SpaceGassApi.Client`) |
| Python imports | `space_gass_api` | (not `spacegass_client`) |

### SDK Generation (Kiota)

- `kiota.config.json` at the root defines both C# and Python targets
- Both point to `descriptions/preview/SpaceGassApi.json` (stable path)
- The `generate-clients` workflow is **manual trigger** (`workflow_dispatch`) with `--clean-output`
- C# output: `sdks/csharp/client/SpaceGassApi/Generated/` — never hand-edit
- Python output: `sdks/python/client/space_gass_api/generated/` — never hand-edit. The `generate-clients` workflow runs `tools/regen_python_inits.py` automatically after Kiota; for local regens, run `python tools/regen_python_inits.py` afterwards.
- Kiota generates a `BaseSpaceGassApiClient` base class (set via `--class-name` in the workflow). The hand-maintained wrappers extend it and expose the public `SpaceGassApiClient` class. Same pattern as the MS Graph SDKs.

### C# Client Structure

```
sdks/csharp/client/
├── SpaceGassApi.sln                     ← client solution (+ future tests)
└── SpaceGassApi/
    ├── SpaceGassApi.csproj              ← hand-maintained (safe from Kiota regen)
    ├── SpaceGassApiClient.cs            ← hand-maintained — SpaceGassApiClient : BaseSpaceGassApiClient
    └── Generated/                       ← Kiota output (wiped on --clean-output)
        ├── BaseSpaceGassApiClient.cs    ← Kiota-generated base client
        ├── Models/
        └── ...
```

- Kiota generates `BaseSpaceGassApiClient` (set via `--class-name` in the workflow). The hand-maintained `SpaceGassApiClient.cs` defines `SpaceGassApiClient : BaseSpaceGassApiClient` which adds `CreateClient()`. Same pattern as the [Microsoft Graph .NET SDK](https://github.com/microsoftgraph/msgraph-sdk-dotnet).
- `.csproj` uses `EnableDefaultCompileItems=false` and explicit `<Compile Include>` for `Generated\**\*.cs` and `SpaceGassApiClient.cs`

### Python Client Structure

```
sdks/python/client/
├── pyproject.toml
└── space_gass_api/
    ├── __init__.py                 ← AUTO-WRITTEN post-Kiota by tools/regen_python_inits.py
    ├── __init__.pyi                ← AUTO-WRITTEN post-Kiota (type stub for IDE support)
    ├── space_gass_api_client.py    ← hand-maintained (SpaceGassApiClient, create_client, _enhance_get_methods)
    ├── models/
    │   └── __init__.py             ← AUTO-WRITTEN post-Kiota (re-exports from generated/)
    └── generated/                  ← Kiota output (wiped on --clean-output)
        ├── base_space_gass_api_client.py  ← Kiota-generated base client (BaseSpaceGassApiClient)
        ├── models/
        └── ...rest is Kiota...
```

- Kiota generates `BaseSpaceGassApiClient` (set via `--class-name` in the workflow) into the `generated/` subfolder with namespace `space_gass_api.generated`. The hand-maintained `space_gass_api_client.py` defines `SpaceGassApiClient(BaseSpaceGassApiClient)` which adds `create_client()` as a static method. Same pattern as the [Microsoft Graph Python SDK](https://github.com/microsoftgraph/msgraph-sdk-python).
- The `generated/` subfolder is the Kiota `--clean-output` target. Hand-maintained files (`__init__.py`, `__init__.pyi`, `space_gass_api_client.py`, `models/__init__.py`) live outside it and survive regeneration.
- The post-regen script `tools/regen_python_inits.py` writes `__init__.py` at the package root and `models/__init__.py` as a re-export shim so callers can write `from space_gass_api import SpaceGassApiClient` and `import space_gass_api.models as models`.
- `space_gass_api/__init__.py` imports `SpaceGassApiClient` from the hand-maintained `space_gass_api_client` module and calls `_enhance_get_methods()` to enable `.get(**kwargs)` on builders.

### Authentication

- **No authentication required** — the API runs locally on the user's machine
- SDK ships with `SpaceGassApiClient.CreateClient()` which uses `AnonymousAuthenticationProvider`
- Default base URL: `http://localhost:34560` — the SDK auto-appends `/api/v1`
- SSL verification is disabled by default (local API may use self-signed certs)
- HTTP↔HTTPS redirects are allowed so either scheme works
- When API key auth is added later, `CreateClient(apiKey: "...")` will be a non-breaking addition

### Examples

- **C# examples** use `ProjectReference` to `../../client/SpaceGassApi/SpaceGassApi.csproj` (will switch to NuGet package reference once published)
- **Python examples** are organized in individual **snake_case folders** (`create_simple_beam/`, `run_analysis/`, etc.)
- C# examples follow `Example.PascalCase` folder naming
- All examples use the one-liner `CreateClient()` factory — no shared helper project needed

### Documentation Site (Zudoku)

- Built with [Zudoku](https://zudoku.dev) v0.69.3
- **`basePath: "/docs"`** is required in `zudoku.config.tsx` — the docs site is served at `https://api.spacegass.com/docs/`
- The deploy workflow uploads `docs/dist/docs` (the inner basePath directory) as the Pages artifact to avoid double-nesting
- A postinstall patch (`docs/patches/fix-zudoku-mjs.js`) fixes a Vite 7 SSR `.mjs` issue
- The API reference reads from `../descriptions/preview/SpaceGassApi.json` (single source of truth)
- `node_modules/` is never committed — `npm ci` regenerates it

### GitHub Pages Deployment

- Source: **GitHub Actions** (not "Deploy from a branch")
- URL: `https://api.spacegass.com/docs/`
- Workflow: `.github/workflows/deploy-docs.yml`
- Uses `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true` to suppress Node 20 deprecation warnings

### CI/CD Workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| `deploy-docs.yml` | Push to `main` | Build Zudoku site and deploy to GitHub Pages |
| `generate-clients.yml` | Manual (`workflow_dispatch`) | Run Kiota to regenerate SDK clients |
| `publish-packages.yml` | GitHub Release published | Publish to NuGet and PyPI |

### Versioning

- SDK versions mirror the SPACE GASS Desktop version (e.g., Desktop v15.0.2 = NuGet `SpaceGassApi 15.0.2`)
- The `descriptions/current/` folder won't exist until the first formal release
- The repo starts in **preview state** with specs in `descriptions/preview/`
