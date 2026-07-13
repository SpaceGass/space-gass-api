# AGENTS.md — SPACE GASS API

Instructions for AI coding agents writing scripts against the SPACE GASS API and its SDKs.
This is a cross-tool convention (read by many coding agents). Claude Code reads it via the
import in [CLAUDE.md](CLAUDE.md).

## What this API is

- **SPACE GASS** is structural-analysis software. This API gives programmatic access to it:
  open/create job files, read and edit structural entities (nodes, members, sections,
  materials, loads), run analyses, and query results.
- It is a **headless LOCAL service** — a server running on the user's own machine. There is
  **no cloud**, **no UI automation**, and **no authentication**.
- Default base URL: `http://localhost:34560`. The SDK auto-appends `/api/v1`, so you never
  write the version segment yourself. Either HTTP or HTTPS works; SSL verification is off by
  default (the local service may use a self-signed cert).
- The service must be running before any call. It ships as the **SPACE GASS API** shortcut
  (`SpaceGassApi.exe`).

## Install

```bash
pip install space-gass-api          # Python 3.9+
dotnet add package SpaceGassApi     # C# / .NET 10 or .NET Standard 2.0+
```

## Minimal usage

The SDKs are generated with [Microsoft Kiota](https://learn.microsoft.com/en-us/openapi/kiota/),
so calls are fluent builder chains that end in the HTTP verb (`get`/`post`/`patch`/`delete`).
Everything is async.

**Python**

```python
from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models

client = SpaceGassApiClient.create_client()          # no auth; base URL defaults to localhost:34560
try:
    await client.job.open_sample.post(models.OpenSampleRequest(file_name="Portal Frame.SG"))
    nodes = await client.job.structure.nodes.get()
    for n in nodes:
        print(n.id, n.x, n.y, n.z)
finally:
    await client.job.close.post()                    # always release the active job
```

**C#**

```csharp
using SpaceGassApi;
using SpaceGassApi.Models;

var client = SpaceGassApiClient.CreateClient();       // no auth; defaults to localhost:34560
try
{
    await client.Job.OpenSample.PostAsync(new OpenSampleRequest { FileName = "Portal Frame.SG" });
    var nodes = await client.Job.Structure.Nodes.GetAsync();
    foreach (var n in nodes!) Console.WriteLine($"{n.Id}: ({n.X},{n.Y},{n.Z})");
}
finally { await client.Job.Close.PostAsync(); }
```

## Rules an agent must follow

1. **One active job.** Open a file (`job.open` / `job.open_sample`) or create one before touching
   structure or results, and `job.close` when done (use `try/finally`). There is a single active
   job per service instance.
2. **Analyses are asynchronous.** Start a run (e.g. `job.analysis.static.run_linear.post(...)`),
   then poll `job.analysis.runs.by_run_id(runId).get()` until `status` is `Completed`, `Failed`,
   or `Cancelled`. Do not assume results exist immediately after starting a run.
3. **Never hand-edit generated code.** Files under `sdks/csharp/client/SpaceGassApi/Generated/`
   and `sdks/python/client/space_gass_api/generated/` are Kiota output and are overwritten.
4. **Python query params are keyword args on the verb call** — e.g. `client.job.structure.nodes.get(node_type=models.NodeTypeFilter.Restrained)` or `client.job.structure.nodes.bulk.post(bodies, continue_on_error=True)`. Works on `get`/`post`/`patch`/`delete` wherever the endpoint defines query parameters; names are the snake_case query-parameter fields.
5. **Filtering by ID lists** uses the SG list-string format (e.g. `"1-5,8,10"`). C# helpers in
   `Utils/ListUtilsExtensions.cs` (`ToFilterString`, `ToIdArray`) convert to/from `int[]`.
6. **File uploads** (`job/new-from-template`, `job/import/txt`) use the multipart helpers
   `NewFromTemplateRequest` / `ImportTxtRequest`, which take a file path.

## Authoritative resources (fetch these; don't crawl the repo)

- **Full docs bundle for LLMs:** <https://api.spacegass.com/docs/llms-full.txt>
- **Docs index:** <https://api.spacegass.com/docs/llms.txt>
- **OpenAPI spec (JSON):** <https://api.spacegass.com/docs/api/1/schema.json>
- **Docs site:** <https://api.spacegass.com/docs/>
- **Repo as an MCP server (search docs/examples/code):** <https://gitmcp.io/SpaceGass/space-gass-api>
- **Runnable examples:** [`sdks/python/examples/`](sdks/python/examples/) · [`sdks/csharp/examples/`](sdks/csharp/examples/)

When fetching individual repo files, use `raw.githubusercontent.com/...` URLs, **never** `github.com/.../blob/...` (those return an HTML page, not the file), and prefer the bundle URLs above so you never need to crawl the repo tree.
