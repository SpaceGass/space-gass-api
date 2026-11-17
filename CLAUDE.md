# CLAUDE.md

Project context and decisions for the `space-gass-api` repository.

## Overview

This is the public developer-facing repo for the SPACE GASS API. It contains the OpenAPI spec, auto-generated Kiota SDKs, hand-crafted examples, and a Zudoku documentation site deployed to GitHub Pages.

### Agent-facing SDK usage

Cross-tool agent instructions (install, `CreateClient()`, base URL, async/analysis rules, key resources) live in `AGENTS.md` at the repo root — imported below so Claude Code loads it too. Keep SDK *usage* guidance in `AGENTS.md`; keep repo *maintenance* decisions in this file.

@AGENTS.md

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

- The single live spec is **`descriptions/openapi.json`** — standard OpenAPI filename convention (tooling and consumers expect it), and a stable path for configs
- The version is embedded inside the spec file itself (`info.x-space-gass-build`) — the filename doesn't carry it

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
- Both point to `build/openapi.kiota.json` — a **transformed copy** of the published spec written by `tools/prepare_spec_for_kiota.py` (git-ignored). See "oneOf and Kiota" below.
- The `generate-clients` workflow is **manual trigger** (`workflow_dispatch`) with `--clean-output`
- C# output: `sdks/csharp/client/SpaceGassApi/Generated/` — never hand-edit
- Python output: `sdks/python/client/space_gass_api/generated/` — never hand-edit. The `generate-clients` workflow runs `tools/regen_python_inits.py` automatically after Kiota; for local regens, run `python tools/regen_python_inits.py` afterwards.
- Kiota generates a `BaseSpaceGassApiClient` base class (set via `--class-name` in the workflow). The hand-maintained wrappers extend it and expose the public `SpaceGassApiClient` class. Same pattern as the MS Graph SDKs.

#### oneOf and Kiota

The published spec (`descriptions/openapi.json`) uses `oneOf` wherever a body or response is one of several polymorphic types — per-code steel design settings (15 codes) and section shapes (41 types). That is the right shape for the API reference (Swagger/Zudoku render a pick-list) but Kiota has no union types: it turns each `oneOf` into a *composed type wrapper* with one nullable property per member (`new X_codeSettings { SteelMemberDesignSettingsAs4100Update = ... }`, `GetAsSettingsGetResponseAsync()`).

Every such `oneOf` lists subclasses of one base schema with a discriminator, so the wire format is the same either way. `tools/prepare_spec_for_kiota.py` therefore writes a copy for Kiota only, in which:

1. each `oneOf` is replaced by a `$ref` to the shared base (`SteelMemberDesignSettingsBase[Update]`, `SectionShape`) → Kiota emits plain inheritance: `PatchAsync(SteelMemberDesignSettingsBaseUpdate body)`, `List<SectionShape> Shapes`, and the base's factory builds the right subclass on read;
2. each subclass's single-value discriminator enum is replaced by a string `default` → Kiota sets it in the constructor (`ShapeType = "Library"`), so callers never set discriminators. (Leaving the enum in as well makes Kiota emit C# that doesn't compile.)

The published spec is never modified. The script exits non-zero if it meets a `oneOf` it can't convert (members without a single shared discriminated base) — decide then whether to extend it or accept a wrapper (`ALLOWED_ONEOF`). `tools/check_helpers.py` fails if any composed wrapper appears in either generated tree. **Any regen path must run the transform first** — the `generate-clients` workflow does; the BuildMachine pipeline (`generate-api-clients.yml` in the SPACEGASS repo) must too.

### C# Client Structure

```
sdks/csharp/client/
├── SpaceGassApi.sln                     ← client solution (+ future tests)
└── SpaceGassApi/
    ├── SpaceGassApi.csproj              ← hand-maintained (safe from Kiota regen)
    ├── SpaceGassApiClient.cs            ← hand-maintained — SpaceGassApiClient : BaseSpaceGassApiClient
    ├── Utils/                           ← hand-maintained helpers (safe from regen)
    │   ├── ListUtilsExtensions.cs       ← SG list-string helpers (ToFilterString, ToIdArray)
    │   ├── UploadRequests.cs            ← NewFromTemplateRequest / ImportTxtRequest (multipart uploads)
    │   └── SteelMemberDesignExtensions.cs ← steel design conveniences: ForCode(DesignCode), typed Settings.GetAsync<T>/PatchAsync<T>
    └── Generated/                       ← Kiota output (wiped on --clean-output)
        ├── BaseSpaceGassApiClient.cs    ← Kiota-generated base client
        ├── Models/
        └── ...
```

- Kiota generates `BaseSpaceGassApiClient` (set via `--class-name` in the workflow). The hand-maintained `SpaceGassApiClient.cs` defines `SpaceGassApiClient : BaseSpaceGassApiClient` which adds `CreateClient()`. Same pattern as the [Microsoft Graph .NET SDK](https://github.com/microsoftgraph/msgraph-sdk-dotnet).
- `.csproj` uses `EnableDefaultCompileItems=false` and explicit `<Compile Include>` for `Generated\**\*.cs`, `SpaceGassApiClient.cs`, and `Utils\**\*.cs`.

#### Hand-maintained additions on top of Kiota

Anything that smooths over awkward raw Kiota output lives **outside `Generated/`** so it survives `--clean-output` — the wrapper `SpaceGassApiClient.cs` and the `Utils/` folder (globbed into the csproj). Add a helper here when the generated surface is clumsy to call by hand:

- **`Utils/ListUtilsExtensions.cs`** — converts between `int[]` and the SG list-string filter format used by query parameters (`ToFilterString()`, `ToIdArray()`, `ToIdList()`).
- **`Utils/UploadRequests.cs`** — `NewFromTemplateRequest` / `ImportTxtRequest` subclass Kiota's `MultipartBody` for the multipart file-upload endpoints (`POST /job/new-from-template`, `POST /job/import/txt`). Kiota types those `PostAsync` parameters as a bare `MultipartBody`; these subclasses let callers write `PostAsync(new NewFromTemplateRequest(path))` — they take a file path, read the bytes, and add the single form part with its filename. No request adapter is set: the request builder attaches it at send time (Kiota's `SetContentFromParsable`).
- **`Utils/SteelMemberDesignExtensions.cs`** — conveniences on top of the (wrapper-free) steel member design surface: `SteelMember.ForCode(DesignCode.As4100)` replaces the string indexer, and `Settings.GetAsync<TSettings>()` / `Settings.PatchAsync<TSettings>(update)` return the code's own settings type instead of `SteelMemberDesignSettingsBase` (throwing `InvalidCastException` on a mismatch). Nothing here is needed to *call* the API — settings objects and shapes are passed directly thanks to the spec transform.

**If a composed wrapper ever shows up in `Generated/`** it means a `oneOf` slipped past `tools/prepare_spec_for_kiota.py` — fix it there (spec transform), not with a helper here.

When a new endpoint is similarly awkward (multipart uploads, list-string filters, etc.), prefer adding a small hand-maintained type/extension here over documenting the raw Kiota boilerplate.

### Python Client Structure

```
sdks/python/client/
├── pyproject.toml
└── space_gass_api/
    ├── __init__.py                 ← AUTO-WRITTEN post-Kiota by tools/regen_python_inits.py
    ├── __init__.pyi                ← AUTO-WRITTEN post-Kiota (type stub for IDE support)
    ├── space_gass_api_client.py    ← hand-maintained (SpaceGassApiClient, create_client, _enhance_request_methods)
    ├── upload_requests.py          ← hand-maintained (NewFromTemplateRequest, ImportTxtRequest)
    ├── steel_member.py             ← hand-maintained (for_code, get_settings, patch_settings)
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
- `space_gass_api/__init__.py` imports `SpaceGassApiClient` from the hand-maintained `space_gass_api_client` module and calls `_enhance_request_methods()` to enable keyword query parameters on builder `get`/`post`/`patch`/`put`/`delete` methods (each verb is enhanced only where a matching `{Verb}QueryParameters` dataclass exists).
- **Hand-maintained additions on top of Kiota** (Python mirror of the C# `Utils/` layer) live at the package root, outside `generated/`: `upload_requests.py` defines `NewFromTemplateRequest` / `ImportTxtRequest`, which subclass Kiota's `MultipartBody` so the multipart file-upload endpoints can be called by file path — `await client.job.new_from_template.post(NewFromTemplateRequest(path))`. They are re-exported from the package root by `tools/regen_python_inits.py` (so `from space_gass_api import NewFromTemplateRequest` works); update that script's `PKG_INIT_*` constants when adding more. `steel_member.py` mirrors the C# `SteelMemberDesignExtensions`: `for_code(client, DesignCode.As4100)`, and `get_settings(code, expect=None)` / `patch_settings(code, update, expect=None)` where `expect` gives a typed return via `@overload`. Importable as `from space_gass_api import steel_member`.

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

- Built with [Zudoku](https://zudoku.dev) v0.82.x
- **`basePath: "/docs"`** is required in `zudoku.config.tsx` — the docs site is served at `https://api.spacegass.com/docs/`
- The deploy workflow uploads `docs/dist/docs` (the inner basePath directory) as the Pages artifact to avoid double-nesting
- A postinstall patch (`docs/patches/fix-zudoku-mjs.js`) fixes a Vite SSR `.mjs` issue (still required as of zudoku 0.82.2)
- The API reference reads from `../descriptions/openapi.json` (single source of truth)
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
- The spec lives at `descriptions/openapi.json` (no `preview/`/`current/` split); the SDK version is taken from `info.x-space-gass-build`
