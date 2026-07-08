# SPACE GASS API

[![Tests](https://github.com/SpaceGass/space-gass-api/actions/workflows/test-clients.yml/badge.svg)](https://github.com/SpaceGass/space-gass-api/actions/workflows/test-clients.yml)
[![NuGet](https://img.shields.io/nuget/v/SpaceGassApi?logo=nuget&label=NuGet)](https://www.nuget.org/packages/SpaceGassApi)
[![PyPI](https://img.shields.io/pypi/v/space-gass-api?logo=pypi&logoColor=white&label=PyPI)](https://pypi.org/project/space-gass-api/)
[![Docs](https://img.shields.io/badge/docs-api.spacegass.com-blue)](https://api.spacegass.com/docs/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Official SPACE GASS API specifications, developer SDKs, and automation examples.

**Developer docs:** [api.spacegass.com/docs](https://api.spacegass.com/docs/)\
**Developer docs (for AI agents):** [api.spacegass.com/docs/llms-full.txt](https://api.spacegass.com/docs/llms-full.txt)

## Overview

The **SPACE GASS API** gives you programmatic access to SPACE GASS structural analysis — open job files, read or edit structural entities, run analyses, and query results. The API is a **headless service** that runs as a local server on your machine; no UI, no cloud round-trip, no authentication required.

This repository contains:

- **OpenAPI specifications** — the canonical API definition used to generate SDKs and documentation
- **SDKs** — auto-generated client libraries for [C#](https://www.nuget.org/packages/SpaceGassApi) (NuGet) and [Python](https://pypi.org/project/space-gass-api/) (PyPI)
- **Examples** — runnable C# and Python programs (see `sdks/*/examples/`)
- **Documentation site** — built with [Zudoku](https://zudoku.dev)

## Quick Start

### Install the SDK

**C# (.NET Standard 2.0+)**

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

For the full walk-through see the [Quick Start](https://api.spacegass.com/docs/getting-started/quick-start). More examples are in `sdks/csharp/examples/` and `sdks/python/examples/`, or clone the repo and browse.

## Using with AI coding agents

Writing scripts against this API with an AI assistant (Claude Code, Cursor, Copilot, ChatGPT, etc.)? Point the agent at the resources below rather than letting it crawl this repo — the docs bundle and OpenAPI spec are single, clean, machine-readable fetches.

- **Full docs bundle for LLMs:** <https://api.spacegass.com/docs/llms-full.txt>
- **Docs index:** <https://api.spacegass.com/docs/llms.txt>
- **OpenAPI spec (JSON):** <https://api.spacegass.com/docs/api/1/schema.json>
- **This repo as an MCP server** (lets an agent search the docs, examples, and code with zero setup): <https://gitmcp.io/SpaceGass/space-gass-api>
- **Repo-root agent instructions:** [`AGENTS.md`](AGENTS.md)

Paste this to prime an agent:

```
You have access to the SPACE GASS structural-analysis API — a LOCAL, no-auth
service at http://localhost:34560 (base path /api/v1). Load these first:
- Full docs bundle:  https://api.spacegass.com/docs/llms-full.txt
- OpenAPI spec:      https://api.spacegass.com/docs/api/1/schema.json
- Repo via GitMCP:   https://gitmcp.io/SpaceGass/space-gass-api

SDKs (Kiota, fluent builder chains, async):
- Python:  pip install space-gass-api    ->  from space_gass_api import SpaceGassApiClient
- C#:      dotnet add package SpaceGassApi
Both expose SpaceGassApiClient.CreateClient() (no auth, base URL auto-set).
Use raw.githubusercontent.com for repo files, never /blob/ URLs.
```

## Descriptions & Client Generation

The C# and Python SDKs are auto-generated using [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) from the current spec (`descriptions/current/`). Previously released specs are kept in `descriptions/archive/` for reference.

The generated client code should never be hand-edited — changes come from updating the OpenAPI spec and re-running the generation workflow.

Kiota generates fluent builder chains that use REST terms explicitly — `GetAsync()`, `PostAsync()`, `PatchAsync()`, `DeleteAsync()` — so the SDK reads like the HTTP calls it makes under the hood. See the [Concepts page](https://api.spacegass.com/docs/getting-started/concepts) for how these map to the API.

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
