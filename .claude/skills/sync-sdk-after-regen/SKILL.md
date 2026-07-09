---
name: sync-sdk-after-regen
description: Use this skill in the space-gass-api repo whenever the OpenAPI spec or the regenerated Kiota SDK clients change — typically right after the `generate-clients` workflow lands a "regenerate SDK clients" commit on `main`, or any time `descriptions/preview/openapi.json` is updated. It brings the hand-written C# and Python examples, the Zudoku docs pages, and the dynamic code-snippet generator back in line with the new SDK surface. Trigger phrases: "regenerated SDKs", "spec updated", "fix examples after regen", "sync after kiota", "update for new build", or after a commit titled "regenerate SDK clients".
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

File: `docs/zudoku.config.tsx`, function `generateCodeSnippet`.

**As of build `14.50.128` the generator reads the request-body type straight from the spec — it does NOT guess from the path, and there is NO `BODY_TYPE_OVERRIDES` map any more.** The helper `bodyTypeFromSpec(operation)` reads the component name from the dereferenced body schema: Zudoku keeps the original pointer on `schema.__$ref` (and `schema.items.__$ref` for bulk/array bodies — see [node_modules/zudoku/src/lib/oas/parser/dereference/index.ts](../../../docs/node_modules/zudoku/src/lib/oas/parser/dereference/index.ts)), so the exact name (`MovingLoadVehicleCreate`, `SectionUserCreate`, …) is always recovered. The old per-regen chore of adding override entries is gone. The path-based `{Entity}Create/Update/Item` derivation survives only as a fallback for inline (un-`$ref`d) bodies.

What to still check after a regen:

1. **`__$ref` still resolves (Zudoku-upgrade guard).** `__$ref` is an undocumented Zudoku internal. If a Zudoku version bump renames or drops it, every snippet silently falls back to the path guess and starts emitting wrong names. Two checks:
   - **Mechanism:** the dereferencer must still write it — `grep -n '__\$ref' docs/node_modules/zudoku/src/lib/oas/parser/dereference/index.ts` must show the assignment (`current.__$ref = $ref`; confirmed present at 0.82.2), and `bodyTypeFromSpec` in `zudoku.config.tsx` still reads `schema.__$ref ?? schema.items.__$ref`.
   - **Schema names still reach the client:** after `npm run build`, grep the built output. Important caveat (verified at zudoku 0.82.2): generated snippet text is **never prerendered into `dist/`** — snippets render client-side only. These greps match the schema names embedded in each API page's route data and the served spec copy, so they catch schema renames/disappearances but can NOT catch a broken `__$ref`:
   ```bash
   cd docs
   for t in MovingLoadVehicleCreate SectionUserCreate MaterialUserCreate CombinationLoadCaseItem; do
     echo "$t -> $(grep -rl "$t" dist/docs | wc -l) file(s)"; done   # all should be >0
   ```
   (`MaterialCreate` was renamed `MaterialUserCreate` server-side between builds 14.50.128 and 14.50.134 — update this list when schemas rename.) If the mechanism check is in doubt (e.g. after a Zudoku upgrade), the only real verification is in a browser: `npm run preview` (serves at `http://localhost:4000/docs`), open an irregular write endpoint (e.g. Moving Load Vehicles → Create) and confirm the C#/Python snippet shows `MovingLoadVehicleCreate`, not the naive path guess `VehicleCreate`.
2. **Builder chain & Python module path** — the chain (`client.Job.Loads…`) and the Python import (`from space_gass_api.models.<snake> import <Type>`) are still derived mechanically. Spot-check one new endpoint's rendered C# and Python snippet.
3. **Filter query params** — unchanged: the generator does NOT emit query params; filtered-query snippets are a docs-page job, not a generator job.

### Naming-consistency sanity check (spec-smell report)

Because the generator now trusts the spec, inconsistent schema naming no longer breaks snippets — but it is a real spec smell worth surfacing to the API team (e.g. a `User` qualifier on one sibling create endpoint but not its peer). Run this to list every write endpoint whose body schema name diverges from the `{Entity}Create/Update/Item` convention its path implies:

```bash
python - <<'PY'
import json
P=json.load(open('descriptions/preview/openapi.json'))['paths']
def pascal(s): return ''.join(w[:1].upper()+w[1:] for w in s.split('-'))
def sing(w): return w[:-3]+'y' if w.endswith('ies') else (w[:-1] if w.endswith('s') else w)
def body(op):
    try: s=op['requestBody']['content']['application/json']['schema']
    except Exception: return None
    return (s.get('$ref') or s.get('items',{}).get('$ref','')).split('/')[-1] or None
for path,ops in sorted(P.items()):
    for m,op in ops.items():
        if m not in ('post','patch','put'): continue
        actual=body(op)
        if not actual: continue
        seg=next((s for s in reversed(path.strip('/').split('/'))
                  if not s.startswith('{') and s not in ('bulk','items')),'')
        implied=f"{pascal(sing(seg))}{'Item' if path.rstrip('/').endswith('items') else ('Create' if m=='post' else 'Update')}"
        if actual!=implied:
            print(f"{m.upper():5} /{path.strip('/'):55} {actual}  (path implies {implied})")
PY
```

This is a **report only** — schema names are a server-side decision; this skill never renames them. Expect a large baseline (54 at builds `14.50.134` and `14.50.139`, unchanged between the two): many flags are **legitimately off-convention by design** and are NOT problems — action bodies (`OpenJobRequest`, `SaveJobRequest`, `MovingLoadGenerateRequest`), shared settings types reused across run/settings endpoints (`BucklingSettingsUpdate`), and consistent domain prefixes (`MovingLoad*`). Don't try to "fix" those. The two signals that *are* actionable:

- **Sibling disagreements** — peer endpoints that should match but don't. The historical example (since resolved server-side): `POST /job/structure/sections` → `SectionUserCreate` but `POST /job/structure/materials` → `MaterialCreate`; by build `14.50.134` materials was renamed `MaterialUserCreate` to match its sibling. New disagreements of this shape read as accidental.
- **Build-over-build deltas** — run the script against the previous spec too and diff; a *new* divergence that doesn't fit an existing pattern usually means the backend's naming drifted in this build.

Put the grouped list (and any sibling disagreements / new deltas called out) in the Phase 6 report so the API team can decide whether to normalise.

## Phase 6 — Report

Summarise per-track files touched, build status, and anything left unverifiable (e.g. "no Python interpreter available, py_compile skipped — relied on visual review and C# build as structural backstop"). Flag any new endpoints in the spec that have no example coverage. Include the naming-consistency report from Phase 5 (the spec-smell list) so the API team can see any new schema-naming inconsistencies this build introduced.

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
| `MaterialCreate` | `MaterialUserCreate` (between `14.50.128` and `14.50.134`) |
| `client.File.Status.PostAsync(new FileStatusRequest {...})` | `client.File.Status.GetAsync(config => config.QueryParameters.FilePath = ...)` |
