---
name: sync-sdk-after-regen
description: Use this skill in the space-gass-api repo whenever the OpenAPI spec or the regenerated Kiota SDK clients change — typically right after the `generate-clients` workflow lands a "regenerate SDK clients" commit on `develop`, or any time `descriptions/preview/openapi.json` is updated. It brings the hand-written C# and Python examples, the Zudoku docs pages, and the dynamic code-snippet generator back in line with the new SDK surface. Trigger phrases: "regenerated SDKs", "spec updated", "fix examples after regen", "sync after kiota", "update for new build", or after a commit titled "regenerate SDK clients".
---

# sync-sdk-after-regen

This skill replays the post-regen sync workflow that was hand-walked for build `14.50.65`. It assumes you are at the repo root of `space-gass-api` and the latest spec + generated SDK clients are committed.

Goal: every example compiles, every doc page references current endpoints/models, the Zudoku docs site builds, and the snippet generator emits valid SDK code.

## Phase 1 — Diff the spec and SDKs

Build the change matrix that drives every later edit:

1. **Spec history** — `git log --oneline -- descriptions/preview/openapi.json` then diff the latest two commits (or against `origin/develop` if working on a feature branch). Note: removed/added paths, renamed query parameters (esp. plural→string SG-list filters like `case`→`cases`), renamed path parameters (`{key}`→`{id}`), and any change to `info.x-space-gass-build`.
2. **C# Generated diff** — `git diff <prev>..HEAD -- sdks/csharp/client/SpaceGassApi/Generated`. Look at:
   - `SpaceGassApiClient.cs` for new/removed top-level builders
   - `Models/` folder additions/removals (typical breaking change: `XCreate` renamed to `XUserCreate`, etc.)
   - `Item/` folder renames
3. **Python Generated diff** — same under `sdks/python/client/space_gass_api`. Python mirrors C# but with snake_case file/property names.
4. **Default port / base URL change** — `grep -rn "localhost:[0-9]\+" .`. The desktop service port has changed historically (e.g. 5000 → 34560). If the spec's `servers[0].url` or any `ServiceInfo` model docstring shows a new host, sweep all hard-coded references in `CLAUDE.md`, `sdks/*/client/.../Extensions/`, every example header comment, and every doc page curl block.
5. **Verify the regen committed cleanly** — `dotnet build sdks/csharp/examples/SpaceGassApi.Examples.sln` against the SDK alone (no example edits yet). If it fails with `CS0234: namespace 'X' does not exist`, the regen committed an inconsistent tree (a builder references a folder that wasn't generated/committed). Fix by re-running `kiota generate` (see [CLAUDE.md](../../../CLAUDE.md) for the full command set, or `.github/workflows/generate-clients.yml`). Don't hand-edit `Generated/`.

Output of this phase: a written change matrix you can refer back to.

## Phase 2 — C# examples

Files: every `Example.*/Program.cs` under `sdks/csharp/examples/`. Apply the change matrix, paying attention to:

- Response model field renames (most common: `.Key` → `.Id` on `Node`, `Member`, `Section`, `Material`, etc.).
- Request body type renames (e.g. `SectionCreate` → `SectionUserCreate`).
- Filter query parameters: collection endpoints now take `string?` properties named `Cases`, `Members`, `Modes`, `Nodes` in **SG list format** (`"1,3-7,10"`) instead of `int[]` arrays. Compose with `string.Join(",", ids)` for arbitrary sets.
- Indexer parameter type: `[int]` typed indexer is preferred; the legacy `[string]` indexer is marked `[Obsolete]`.

Verify: `dotnet build sdks/csharp/examples/SpaceGassApi.Examples.sln --nologo`. **Build must be 0 errors before moving on.**

## Phase 3 — Python examples

Files: every entry-point `.py` under `sdks/python/examples/*/`. Mirror Phase 2 with snake_case:

- `.key` → `.id` on response models
- `by_key(...)` → `by_id(...)` on collection indexers (also `by_run_id` etc. for non-`id` path params — leave those alone)
- `case_` (legacy attribute name) → `case` on `NodeReaction`/`Buckling*`/etc.
- `keys=[...]` → `nodes="1,2,3"` for reactions filters
- `from space_gass_api.models.section_create import SectionCreate` → `from space_gass_api.models.section_user_create import SectionUserCreate`
- Drop list arguments to `case_`/`member`/`mode` filter setattrs in favour of `cases`/`members`/`modes` with SG-list strings

Verify: `python -m py_compile <each entry-point>` (Python interpreter must be on PATH; if not, do a careful visual diff and rely on the C# build as a structural backstop). The two SDKs share the same shape, so anything that landed cleanly in C# almost always lands cleanly in Python.

## Phase 4 — Docs MDX

Files: `docs/pages/**/*.mdx`. Use `grep -rn "\.Key\|\.key\|by_key\|case_\|FileStatusRequest\|SectionCreate\|case=\d\|member=\d\|node=\d\|mode=\d\|QueryParameters\.\(Case\|Member\|Mode\|Node\)\b" docs/pages` to find every stale reference, then patch:

- `quick-start.mdx`, `simple-beam.mdx`: `.Key`/`.key` → `.Id`/`.id`, `by_key` → `by_id`, `case_` → `case`
- `filtering-and-querying.mdx` (the heaviest): rewrite filter examples to use the SG list-string format. C#: `config.QueryParameters.Cases = "1,3"`; Python: `setattr(c.query_parameters, 'cases', '1,3')`; curl: `?cases=1,3&nodes=10-12`. Update prose ("Access any entity by its key" → "by its Id").
- `file-handling.mdx`: `client.File.Status.PostAsync(new FileStatusRequest{...})` → `client.File.Status.GetAsync(config => config.QueryParameters.FilePath = ...)`. The endpoint changed from POST-with-body to GET-with-query.
- `error-handling.mdx`: `nodes.by_key(999)` → `nodes.by_id(999)`.
- `versioning.mdx`: confirm version table; mention the new `info.x-space-gass-build` value in passing if relevant.

Do NOT introduce hand-rolled curl URLs that expand request body fields as query string — only the endpoints whose spec changed (e.g. `/file/status`).

Verify: `cd docs && npm ci && npm run build`. The Zudoku build must succeed and produce `docs/dist/docs/`. If the Vite SSR `.mjs` patch fires (postinstall), that's expected — see [docs/patches/fix-zudoku-mjs.js](../../../docs/patches/fix-zudoku-mjs.js).

## Phase 5 — Snippet generator audit

File: `docs/zudoku.config.tsx`, function `generateCodeSnippet`. The function derives builder chains and body type names heuristically — re-test it against the spec's surface:

1. **Python module path** — must use `space_gass_api.models.*`, not any historical alias.
2. **Bulk endpoints** (`/.../bulk` POST) — these take a list of the parent entity, not a `BulkCreate`. Skip "bulk" when computing `entityName`, and emit `List<XCreate>` (C#) / `[XCreate(...)]` (Python).
3. **Body-type overrides** — there is a `BODY_TYPE_OVERRIDES` map keyed by `"${METHOD} ${path}"` for endpoints whose request schema doesn't follow `{Entity}Create`/`{Entity}Update`. Add entries for any new mismatches (e.g. `SectionUserCreate`, `SectionLibraryCreate`).
4. **Filter query params** — the generator does NOT currently emit query params; if a filtered query endpoint needs a snippet, that's a docs-page job, not a generator job. Don't try to inline filters here.

Verify by spot-checking 3 endpoints in the rendered docs after `npm run build`:
- one new endpoint (e.g. a `combination-cases` POST)
- one renamed-parameter endpoint (e.g. a `load-cases/{id}` PATCH)
- one bulk endpoint

## Phase 6 — Report

Summarise per-track files touched, build status, and anything left unverifiable (e.g. "no Python interpreter available, py_compile skipped — relied on visual review and C# build as structural backstop"). Flag any new endpoints in the spec that have no example coverage.

## Out of scope for this skill

- Regenerating the SDK itself (that's the `generate-clients` workflow). If you must regenerate locally, follow the exact `kiota generate` flags from `.github/workflows/generate-clients.yml` to avoid drift, and **commit `Generated/` files separately from example/doc edits**.
- Adding new examples or doc pages — this skill keeps existing material in sync, it doesn't expand coverage.
- A changelog page (deferred — revisit on a future regen).

## Reference: known model/property migrations

Keep this short — the diff in Phase 1 is the source of truth. These are confirmed migrations seen at build `14.50.65`:

| Old | New |
|---|---|
| `Node.Key` / `Member.Key` / `Section.Key` / `Material.Key` | `.Id` |
| `WithKeyRequestBuilder` (path `{key}`) | `LoadCasesItemRequestBuilder` etc. (path `{id}`) |
| `by_key(int)` | `by_id(int)` |
| `case`/`member`/`mode`/`node` query params (array) | `cases`/`members`/`modes`/`nodes` (string, SG list format `"1,3-7,10"`) |
| Python `r.case_` (NodeReaction etc.) | `r.case` |
| `SectionCreate` | `SectionUserCreate` |
| `client.File.Status.PostAsync(new FileStatusRequest {...})` | `client.File.Status.GetAsync(config => config.QueryParameters.FilePath = ...)` |
