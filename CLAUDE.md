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

- `kiota.config.json` at the root defines both C# and Python targets
- Both point to `descriptions/preview/openapi.json` (stable path)
- The `generate-clients` workflow is **manual trigger** (`workflow_dispatch`) with `--clean-output`
- C# output: `sdks/csharp/client/SpaceGassApi/Generated/` — never hand-edit
- Python output: `sdks/python/client/space_gass_api/` — never hand-edit, **except** the `__init__.py` and `__init__.pyi` files which are written by `tools/regen_python_inits.py` after every regen. The `generate-clients` workflow runs that script automatically; for local Kiota regens, run `python tools/regen_python_inits.py` afterwards.
- Both Kiota configs use `clientClassName: "BaseSpaceGassApiClient"` but Kiota strips the namespace prefix, so the generated class is actually called `ApiClient` (in `ApiClient.cs` / `api_client.py`). The hand-maintained wrappers extend `ApiClient` and expose the public `SpaceGassApiClient` class. Same pattern as the MS Graph SDKs.

### C# Client Structure

```
sdks/csharp/client/
├── SpaceGassApi.sln                     ← client solution (+ future tests)
└── SpaceGassApi/
    ├── SpaceGassApi.csproj              ← hand-maintained (safe from Kiota regen)
    ├── Extensions/                      ← hand-maintained
    │   └── SpaceGassApiClient.cs        ← SpaceGassApiClient : ApiClient
    └── Generated/                       ← Kiota output (wiped on --clean-output)
        ├── ApiClient.cs                 ← Kiota-generated base client
        ├── Models/
        └── ...
```

- Kiota generates `ApiClient` (from `clientClassName` in `kiota.config.json`). The hand-maintained `Extensions/SpaceGassApiClient.cs` defines `SpaceGassApiClient : ApiClient` which adds `CreateClient()`. Same pattern as the [Microsoft Graph .NET SDK](https://github.com/microsoftgraph/msgraph-sdk-dotnet).
- `.csproj` uses `EnableDefaultCompileItems=false` and explicit `<Compile Include>` for `Generated\**\*.cs` and `Extensions\**\*.cs`

### Python Client Structure

```
sdks/python/client/
├── pyproject.toml                  ← installs space_gass_api/ + the hand-maintained client module
├── space_gass_api_client.py        ← hand-maintained (SpaceGassApiClient, create_client, _enhance_get_methods) — NEVER touched by Kiota
└── space_gass_api/                 ← Kiota output (wiped on --clean-output)
    ├── __init__.py                 ← AUTO-WRITTEN post-Kiota by tools/regen_python_inits.py
    ├── __init__.pyi                ← AUTO-WRITTEN post-Kiota (type stub for IDE support)
    ├── api_client.py               ← Kiota-generated base client (ApiClient)
    ├── models/
    │   └── __init__.py             ← AUTO-WRITTEN post-Kiota (re-exports every model class)
    └── ...rest is Kiota...
```

- Kiota generates `BaseSpaceGassApiClient` (set via `clientClassName` in `kiota.config.json`). The hand-maintained `space_gass_api_client.py` defines `SpaceGassApiClient(BaseSpaceGassApiClient)` which adds `create_client()` as a static method. This follows the same pattern as the [Microsoft Graph Python SDK](https://github.com/microsoftgraph/msgraph-sdk-python).
- The post-regen script `tools/regen_python_inits.py` writes `__init__.py` files inside the Kiota tree so callers can write `from space_gass_api import SpaceGassApiClient` and `import space_gass_api.models as models`. Without these aggregators, Kiota's PEP 420 namespace package layout means `models.NodeCreate` doesn't resolve.
- The hand-maintained `space_gass_api_client.py` defines `SpaceGassApiClient(ApiClient)` with `create_client()` and `_enhance_get_methods()`. Same pattern as the [Microsoft Graph Python SDK](https://github.com/microsoftgraph/msgraph-sdk-python).
- `space_gass_api/__init__.py` imports `SpaceGassApiClient` from the hand-maintained `space_gass_api_client` module and calls `_enhance_get_methods()` to enable `.get(**kwargs)` on builders.
- `pyproject.toml` uses `[tool.setuptools] py-modules = ["space_gass_api_client"]` to install the hand-maintained module alongside the `space_gass_api` package.

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
