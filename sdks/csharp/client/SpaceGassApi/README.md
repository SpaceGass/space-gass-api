# SpaceGassApi

Official .NET SDK for the SPACE GASS API.

The SPACE GASS API gives you programmatic access to SPACE GASS structural analysis — open or create job files, build and edit structural models, run analyses, and query results. The API runs as a **local service** on your machine with **no authentication**.

## Install

```bash
dotnet add package SpaceGassApi
```

- Targets **.NET 10** and **.NET Standard 2.0/2.1** (.NET Framework 4.6.1+, .NET Core 2.0+, .NET 5/6/8+)
- [SPACE GASS](https://www.spacegass.com) **14.5 or later** installed with an active licence
- The SPACE GASS API service running locally (default: `http://localhost:34560`)

## Quick start

```csharp
using SpaceGassApi;
using SpaceGassApi.Models;

var client = SpaceGassApiClient.CreateClient();   // no auth; defaults to http://localhost:34560

try
{
    // Open a built-in sample project
    await client.Job.OpenSample.PostAsync(
        new OpenSampleRequest { FileName = "Portal Frame.SG" });

    // List all nodes in the model
    var nodes = await client.Job.Structure.Nodes.GetAsync();
    foreach (var n in nodes!)
        Console.WriteLine($"Node {n.Id}: ({n.X}, {n.Y}, {n.Z})");
}
finally
{
    await client.Job.Close.PostAsync();           // always release the active job
}
```

## Run an analysis and query results

```csharp
var client = SpaceGassApiClient.CreateClient();

try
{
    await client.Job.Open.PostAsync(
        new OpenJobRequest { FilePath = @"C:\Models\MyProject.sg" });

    // Analyses are asynchronous: start a run, then poll for completion.
    var run = await client.Job.Analysis.Static.RunLinear.PostAsync(
        new StaticSettingsUpdate());

    AnalysisRun result;
    do
    {
        await Task.Delay(500);
        result = (await client.Job.Analysis.Runs[run!.RunId!.Value].GetAsync())!;
    }
    while (result.Status is not (AnalysisRunStatus.Completed
                              or AnalysisRunStatus.Failed
                              or AnalysisRunStatus.Cancelled));

    // Query node reactions
    var reactions = await client.Job.Query.Analysis.Static.NodeReactions.GetAsync();
    foreach (var r in reactions!.Results!)
        Console.WriteLine($"Node {r.Node}, LC {r.LoadCase}: Fy={r.Fy:F2} kN");
}
finally
{
    await client.Job.Close.PostAsync();
}
```

## How this SDK is structured

Most of this SDK is generated from the OpenAPI specification with
[Microsoft Kiota](https://learn.microsoft.com/en-us/openapi/kiota/). Every endpoint is a
**fluent builder chain that ends in the HTTP verb** — `await client.Job.Structure.Nodes.GetAsync()`,
`...PostAsync(body)`, `...PatchAsync(body)`, `...DeleteAsync()`. Path parameters use indexers
(e.g. `client.Job.Analysis.Runs[runId]`). If an endpoint isn't shown in these examples, the same
pattern applies — browse the [API Reference](https://api.spacegass.com/docs/api).

On top of the generated client, a few **hand-written conveniences** (below) smooth the rough
edges. Everything not listed there is standard Kiota.

## Conveniences on top of Kiota

**`SpaceGassApiClient.CreateClient(baseUrl)`** — one-line factory. Configures anonymous auth,
appends `/api/v1` to the base URL, disables SSL verification (the local service may use a
self-signed certificate), allows HTTP↔HTTPS redirects, and sets a long timeout for analyses.
Pass `baseUrl` only if the service runs on a non-default port (use `https://` for HTTPS).

**ID-list filter helpers** (`SpaceGassApi.Utils`) — convert between `int` collections and the
compact SPACE GASS filter-string format (`"1,3-7,10"`) used by query parameters:

```csharp
using SpaceGassApi.Utils;

// int collection -> compact filter string (sorted, de-duplicated, ranges collapsed)
string filter = new[] { 1, 2, 3, 5, 8 }.ToFilterString();   // "1-3,5,8"

// filter string -> ints (ranges expanded)
int[] ids = "1-3,5,8".ToIdArray();                          // { 1, 2, 3, 5, 8 }
List<int> idList = "1-3,5,8".ToIdList();
```

**File uploads by path** — `NewFromTemplateRequest` / `ImportTxtRequest` wrap the multipart
upload endpoints so you can pass a file path directly:

```csharp
await client.Job.NewFromTemplate.PostAsync(
    new NewFromTemplateRequest(@"C:\Templates\design.sgbase"));
await client.Job.Import.Txt.PostAsync(
    new ImportTxtRequest(@"C:\Data\model.txt"));
```

## Using with an AI assistant

Writing scripts with an AI coding agent? Point it at these single, machine-readable entry
points rather than letting it crawl the source repo:

- Full docs bundle for LLMs: <https://api.spacegass.com/docs/llms-full.txt>
- OpenAPI spec (JSON): <https://api.spacegass.com/docs/api/1/schema.json>
- Repo as an MCP server (search docs, examples, code): <https://gitmcp.io/SpaceGass/space-gass-api>

## Documentation

- [Quick Start](https://api.spacegass.com/docs/quick-start)
- [Concepts](https://api.spacegass.com/docs/concepts)
- [API Reference](https://api.spacegass.com/docs/api)
- [Examples](https://github.com/SpaceGass/space-gass-api/tree/main/sdks/csharp/examples)
