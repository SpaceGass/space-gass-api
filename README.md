# SPACE GASS API

Official SPACE GASS API specifications, developer SDKs, and automation examples.

**Developer docs:** [spacegass.github.io/space-gass-api](https://spacegass.github.io/space-gass-api/)

## Overview

The **SPACE GASS API** gives you programmatic access to SPACE GASS structural analysis — open job files, read or edit structural entities, run analyses, and query results. The API is a **headless service** that runs as a local server on your machine; no UI, no cloud round-trip, no authentication required.

This repository contains:

- **OpenAPI specifications** — the canonical API definition used to generate SDKs and documentation
- **SDKs** — auto-generated client libraries for [C#](https://www.nuget.org/packages/SpaceGassApi) (NuGet) and [Python](https://pypi.org/project/space-gass-api/) (PyPI)
- **Examples** — runnable C# and Python programs (see `sdks/*/examples/`)
- **Documentation site** — built with [Zudoku](https://zudoku.dev)

## Quick Start

### Install the SDK

**C# (.NET 8+)**

```bash
dotnet new console -n MyApp && cd MyApp
dotnet add package SpaceGassApi
```

**Python (3.10+)**

```bash
pip install space-gass-api
```

### Try it — open a built-in sample, list its nodes

Start the SPACE GASS API service (the **SPACE GASS API** shortcut, or `SpaceGassApi.exe`), then run:

**C#**

```csharp
using SpaceGassApi;
using SpaceGassApi.Models;

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");

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

**Python**

```python
from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models

client = SpaceGassApiClient.create_client("http://localhost:34560")

try:
    await client.job.open_sample.post(
        models.OpenSampleRequest(file_name="Portal Frame.SG"))

    nodes = await client.job.structure.nodes.get()
    for n in nodes:
        print(f"Node {n.id}: ({n.x}, {n.y}, {n.z})")
finally:
    await client.job.close.post()
```

For the full walk-through see the [Quick Start](https://spacegass.github.io/space-gass-api/getting-started/quick-start). More examples are in `sdks/csharp/examples/` and `sdks/python/examples/`, or clone the repo and browse.

## Descriptions & Client Generation

The C# and Python SDKs are auto-generated using [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) from the current spec (`descriptions/current/`). Previously released specs are kept in `descriptions/archive/` for reference.

The generated client code should never be hand-edited — changes come from updating the OpenAPI spec and re-running the generation workflow.

Kiota generates fluent builder chains that use REST terms explicitly — `GetAsync()`, `PostAsync()`, `PatchAsync()`, `DeleteAsync()` — so the SDK reads like the HTTP calls it makes under the hood. See the [Concepts page](https://spacegass.github.io/space-gass-api/getting-started/concepts) for how these map to the API.

## Repository Structure

```
space-gass-api/
├── descriptions/       # OpenAPI specifications
│   ├── current/        # Latest released spec (SDKs are generated from this)
│   └── archive/        # Previously released versions
├── sdks/
│   ├── csharp/
│   │   ├── client/     # Auto-generated Kiota client (do not hand-edit)
│   │   └── examples/   # Hand-crafted C# examples
│   └── python/
│       ├── client/     # Auto-generated Kiota client
│       └── examples/   # Hand-crafted Python examples
├── tools/              # Repo-level helper scripts
├── sandbox/            # Informal scripts and experiments
└── docs/               # Developer documentation site (Zudoku)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved.

## Licensing

- **SDKs, examples, and sandbox scripts** — [MIT](LICENSE)
- **OpenAPI specifications** (`descriptions/`) — subject to the [SPACE GASS End User Licence Agreement](https://www.spacegass.com/manual/Introduction/End_User_Licence_Agreement.htm)
