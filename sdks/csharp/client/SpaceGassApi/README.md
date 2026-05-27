# SpaceGassApi

Official .NET SDK for the SPACE GASS API.

The SPACE GASS API gives you programmatic access to SPACE GASS structural analysis — open or create job files, build and edit structural models, run analyses, and query results. The API runs as a local service on your machine with no authentication required.

## Compatibility

- Targets **.NET Standard 2.0** and **.NET Standard 2.1**
- .NET Framework 4.6.1+, .NET Core 2.0+, .NET 5+, .NET 6+, .NET 8+

## Prerequisites

- [SPACE GASS](https://www.spacegass.com) installed with an active licence
- The SPACE GASS API service running locally (default: `http://localhost:34560`)

## Quick Start

```csharp
using SpaceGassApi;
using SpaceGassApi.Models;

var client = SpaceGassApiClient.CreateClient();

try
{
    // Open a built-in sample project
    await client.Job.OpenSample.PostAsync(
        new OpenSampleRequest { FileName = "Portal Frame.SG" });

    // List all nodes in the model
    var nodes = await client.Job.Structure.Nodes.GetAsync();
    foreach (var n in nodes!)
        Console.WriteLine($"Node {n.Id}: ({n.X}, {n.Y}, {n.Z})");

    // List all members
    var members = await client.Job.Structure.Members.GetAsync();
    foreach (var m in members!)
        Console.WriteLine($"Member {m.Id}: Node {m.NodeA} -> Node {m.NodeB}");
}
finally
{
    await client.Job.Close.PostAsync();
}
```

## Run an Analysis and Query Results

```csharp
var client = SpaceGassApiClient.CreateClient();

try
{
    await client.Job.Open.PostAsync(
        new OpenJobRequest { FilePath = @"C:\Models\MyProject.sg" });

    // Run a linear static analysis with current settings
    var run = await client.Job.Analysis.Static.RunLinear.PostAsync(
        new StaticSettingsUpdate());

    // Poll until complete
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

## Documentation

- [Getting Started](https://api.spacegass.com/docs/getting-started/quick-start)
- [API Reference](https://api.spacegass.com/docs/api)
- [Examples](https://github.com/Spacegass/space-gass-api/tree/main/sdks/csharp/examples)
