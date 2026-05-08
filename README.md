# SPACE GASS API

Official SPACE GASS API specifications, developer SDKs, and automation examples.

📖 **Developer docs:** [https://spacegass.github.io/space-gass-api/](https://spacegass.github.io/space-gass-api/)

## Overview

The **SPACE GASS API** gives you programmatic access to SPACE GASS structural analysis — open job files, read or edit structural entities, run analyses, and query results. The API is a **headless service** that runs as a local server on your machine; no UI, no cloud round-trip, no authentication required.

This repository is its public home, containing:

- **OpenAPI specifications** — the canonical API definition used to generate SDKs and documentation
- **SDKs** — auto-generated client libraries for [C#](https://www.nuget.org/packages/SpaceGassApi) (NuGet) and [Python](https://pypi.org/project/space-gass-api/) (PyPI)
- **Examples** — hand-crafted, runnable C# and Python programs
- **Documentation site** — built with [Zudoku](https://zudoku.dev)

## Quick Start

### Install

<table>
<tr><th>C# (.NET 8+)</th><th>Python (3.10+)</th></tr>
<tr><td>

```bash
dotnet new console -n MyApp && cd MyApp
dotnet add package SpaceGassApi
```

</td><td>

```bash
pip install space-gass-api
```

</td></tr>
</table>

### Try it — open a built-in sample, list its nodes

Start the SPACE GASS API service (the **SPACE GASS API** shortcut, or `SpaceGassApi.exe`), then run:

<table>
<tr><th>C#</th><th>Python</th></tr>
<tr><td>

```csharp
using SpaceGassApi;
using SpaceGassApi.Models;

var client = SpaceGassApiClient.CreateClient();

try
{
    await client.Job.OpenSample.PostAsync(
        new OpenSampleRequest { FileName = "Portal Frame.SG" });

    var nodes = await client.Job.Structure.Nodes.GetAsync();
    foreach (var n in nodes!)
        Console.WriteLine($"Node {n.Id}: ({n.X}, {n.Y}, {n.Z})");
}
finally
{
    await client.Job.Close.PostAsync();
}
```

</td><td>

```python
from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models

client = SpaceGassApiClient.create_client()

try:
    await client.job.open_sample.post(
        models.OpenSampleRequest(file_name="Portal Frame.SG"))

    nodes = await client.job.structure.nodes.get()
    for n in nodes:
        print(f"Node {n.id}: ({n.x}, {n.y}, {n.z})")
finally:
    await client.job.close.post()
```

</td></tr>
</table>

For the full guided walk-through see the [Quick Start](https://spacegass.github.io/space-gass-api/getting-started/quick-start) and the [Concepts page](https://spacegass.github.io/space-gass-api/getting-started/concepts).

## Examples

Each folder is a runnable program with its own README. Clone the repo, change into one, and run.

| Example | Description | C# | Python |
|---|---|---|---|
| **Quick Start** | Open `Portal Frame.SG`, list nodes, close. The Quick Start docs page as a runnable program. | [`Example.QuickStart`](sdks/csharp/examples/Example.QuickStart) | [`quick_start`](sdks/python/examples/quick_start) |
| **Create Simple Beam** | Build a simply-supported beam from scratch, run a linear static analysis, query the maximum bending moment + deflection. The full pipeline. | [`Example.CreateSimpleBeam`](sdks/csharp/examples/Example.CreateSimpleBeam) | [`create_simple_beam`](sdks/python/examples/create_simple_beam) |
| **Run Analysis** | Open an existing `.sg`, run analysis with progress polling, print result summary. | [`Example.RunAnalysis`](sdks/csharp/examples/Example.RunAnalysis) | [`run_analysis`](sdks/python/examples/run_analysis) |
| **Analysis Monitor** | A console app that renders real-time analysis progress (current step, percentage, load-case status). Sample app — Windows only. | [`Example.AnalysisMonitor`](sdks/csharp/examples/Example.AnalysisMonitor) | — |
| **Query Restrained Nodes** | Filter to support nodes via `NodeType=Restrained`, then read reactions for just those nodes. | [`Example.QueryRestrainedNodes`](sdks/csharp/examples/Example.QueryRestrainedNodes) | [`query_restrained_nodes`](sdks/python/examples/query_restrained_nodes) |
| **Manage Sections & Materials** | CRUD on sections and materials in a fresh project — create, list, update, attach to a member, delete. | [`Example.ManageSectionsAndMaterials`](sdks/csharp/examples/Example.ManageSectionsAndMaterials) | [`manage_sections_and_materials`](sdks/python/examples/manage_sections_and_materials) |
| **Service Automation** | Probe / start / wait / stop the SPACE GASS API service from your own code, with proper cleanup. | [`Example.ServiceAutomation`](sdks/csharp/examples/Example.ServiceAutomation) | [`service_automation`](sdks/python/examples/service_automation) |

Shorter copy-paste recipes for common single-task questions live in the [Recipes section](https://spacegass.github.io/space-gass-api/guides/examples/recipes/open-your-own-file) of the docs.

## Repository Structure

```
space-gass-api/
├── descriptions/       # OpenAPI specifications (CC BY-ND 4.0)
│   ├── preview/        # Pre-release spec (subject to breaking changes)
│   └── archive/        # Previous released versions
├── sdks/
│   ├── csharp/
│   │   ├── client/     # Auto-generated Kiota client (do not hand-edit)
│   │   └── examples/   # Hand-crafted C# examples
│   └── python/
│       ├── client/     # Auto-generated Kiota client + space_gass_api_extensions.py
│       └── examples/   # Hand-crafted Python examples
├── tools/              # Repo-level helper scripts (e.g. post-Kiota __init__ regenerator)
├── sandbox/            # Informal scripts and experiments
└── docs/               # Developer documentation site (Zudoku)
```

## Versioning

SDK and package versions mirror the SPACE GASS Desktop version. For example, SPACE GASS Desktop v14.5.0 corresponds to `SpaceGassApi 14.5.x` on NuGet and `space-gass-api==14.5.x` on PyPI. Each minor release is sourced from `info.x-space-gass-build` in the OpenAPI spec.

The current preview build is shown in the [API Reference label](https://spacegass.github.io/space-gass-api/api) on the docs site.

## Licensing

This repository uses a dual-license strategy:

| Content | License |
|---|---|
| SDKs, examples, and sandbox scripts | [MIT](LICENSE) |
| OpenAPI specifications (`descriptions/`) | [CC BY-ND 4.0](LICENSE-SPEC) |

The MIT license gives you full freedom to use, modify, and distribute the SDK code. The CC BY-ND license protects the integrity of the API specification while still allowing you to use it freely.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved.
