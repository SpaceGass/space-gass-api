# space-gass-api

Official Python SDK for the SPACE GASS API.

The SPACE GASS API gives you programmatic access to SPACE GASS structural analysis — open or create job files, build and edit structural models, run analyses, and query results. The API runs as a **local service** on your machine with **no authentication**.

## Install

```bash
pip install space-gass-api
```

- Python 3.9+
- [SPACE GASS](https://www.spacegass.com) **14.5 or later** installed with an active licence
- The SPACE GASS API service running locally (default: `http://localhost:34560`)

## Quick start

```python
import asyncio
from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models

async def main():
    client = SpaceGassApiClient.create_client()   # no auth; defaults to http://localhost:34560

    try:
        # Open a built-in sample project
        await client.job.open_sample.post(
            models.OpenSampleRequest(file_name="Portal Frame.SG"))

        # List all nodes in the model
        nodes = await client.job.structure.nodes.get()
        for n in nodes:
            print(f"Node {n.id}: ({n.x}, {n.y}, {n.z})")
    finally:
        await client.job.close.post()             # always release the active job

asyncio.run(main())
```

## Run an analysis and query results

```python
import asyncio
from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models

async def main():
    client = SpaceGassApiClient.create_client()

    try:
        await client.job.open.post(
            models.OpenJobRequest(file_path=r"C:\Models\MyProject.sg"))

        # Analyses are asynchronous: start a run, then poll for completion.
        run = await client.job.analysis.static.run_linear.post(
            models.StaticSettingsUpdate())

        while True:
            await asyncio.sleep(0.5)
            result = await client.job.analysis.runs.by_run_id(str(run.run_id)).get()
            if result.status in (
                models.AnalysisRunStatus.Completed,
                models.AnalysisRunStatus.Failed,
                models.AnalysisRunStatus.Cancelled,
            ):
                break

        # Query node reactions
        reactions = await client.job.query.analysis.static.node_reactions.get()
        for r in reactions.results:
            print(f"Node {r.node}, LC {r.load_case}: Fy={r.fy:.2f} kN")
    finally:
        await client.job.close.post()

asyncio.run(main())
```

## How this SDK is structured

Most of this SDK is generated from the OpenAPI specification with
[Microsoft Kiota](https://learn.microsoft.com/en-us/openapi/kiota/). Every endpoint is a
**fluent builder chain that ends in the HTTP verb** — `await client.job.structure.nodes.get()`,
`...post(body)`, `...patch(body)`, `...delete()`. Path parameters use `.by_*()` selectors
(e.g. `client.job.analysis.runs.by_run_id(run_id)`). If an endpoint isn't shown in these
examples, the same pattern applies — browse the
[API Reference](https://api.spacegass.com/docs/api).

On top of the generated client, a few **hand-written conveniences** (below) smooth the rough
edges. Everything not listed there is standard Kiota.

## Conveniences on top of Kiota

**`SpaceGassApiClient.create_client(base_url=...)`** — one-line factory. Configures anonymous
auth, appends `/api/v1` to the base URL, disables SSL verification (the local service may use a
self-signed certificate), allows HTTP↔HTTPS redirects, and sets a long timeout for analyses.
Pass `base_url` only if the service runs on a non-default port (use `https://` for HTTPS).

**Keyword query parameters on `.get()`** — pass query parameters directly instead of the verbose
`RequestConfiguration` pattern. Names are the snake_case query fields; invalid names raise
`TypeError`. Fully type-stubbed, so IDE autocomplete works.

```python
# Keyword form (enhanced)
nodes = await client.job.structure.nodes.get(
    node_type=models.NodeTypeFilter.Restrained)
reactions = await client.job.query.analysis.static.node_reactions.get(
    cases="1,3-7", nodes="10-12")     # ID-list filters use the SG format "1,3-7,10"

# Verbose form (still supported for advanced use)
from kiota_abstractions.base_request_configuration import RequestConfiguration
from space_gass_api.generated.job.structure.nodes.nodes_request_builder import (
    NodesRequestBuilder,
)
qp = NodesRequestBuilder.NodesRequestBuilderGetQueryParameters(
    node_type=models.NodeTypeFilter.Restrained)
nodes = await client.job.structure.nodes.get(
    request_configuration=RequestConfiguration(query_parameters=qp))
```

**File uploads by path** — `NewFromTemplateRequest` / `ImportTxtRequest` wrap the multipart
upload endpoints so you can pass a file path directly:

```python
from space_gass_api import NewFromTemplateRequest, ImportTxtRequest

await client.job.new_from_template.post(NewFromTemplateRequest("design.sgbase"))
await client.job.import_.txt.post(ImportTxtRequest("model.txt"))
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
- [Examples](https://github.com/SpaceGass/space-gass-api/tree/main/sdks/python/examples)
