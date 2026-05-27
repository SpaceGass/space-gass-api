# space-gass-api

Official Python SDK for the SPACE GASS API.

The SPACE GASS API gives you programmatic access to SPACE GASS structural analysis — open or create job files, build and edit structural models, run analyses, and query results. The API runs as a local service on your machine with no authentication required.

## Compatibility

- Python 3.9+

## Prerequisites

- [SPACE GASS](https://www.spacegass.com) installed with an active licence
- The SPACE GASS API service running locally (default: `http://localhost:34560`)

## Quick Start

```python
import asyncio
from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models

async def main():
    client = SpaceGassApiClient.create_client()

    try:
        # Open a built-in sample project
        await client.job.open_sample.post(
            models.OpenSampleRequest(file_name="Portal Frame.SG"))

        # List all nodes in the model
        nodes = await client.job.structure.nodes.get()
        for n in nodes:
            print(f"Node {n.id}: ({n.x}, {n.y}, {n.z})")

        # List all members
        members = await client.job.structure.members.get()
        for m in members:
            print(f"Member {m.id}: Node {m.node_a} -> Node {m.node_b}")
    finally:
        await client.job.close.post()

asyncio.run(main())
```

## Run an Analysis and Query Results

```python
import asyncio
from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models

async def main():
    client = SpaceGassApiClient.create_client()

    try:
        await client.job.open.post(
            models.OpenJobRequest(file_name=r"C:\Models\MyProject.sg"))

        # Run a linear static analysis with current settings
        run = await client.job.analysis.static.run_linear.post(
            models.StaticSettingsUpdate())

        # Poll until complete
        while True:
            await asyncio.sleep(0.5)
            result = await client.job.analysis.runs.by_run_id(
                str(run.run_id)).get()
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

## Enhanced `.get()` with keyword arguments

The SDK enhances Kiota-generated `.get()` methods so you can pass query
parameters as keyword arguments directly instead of the verbose
`RequestConfiguration` pattern:

```python
# Simple — keyword arguments
nodes = await client.job.structure.nodes.get(
    node_type=models.NodeTypeFilter.Restrained)

# Verbose — also supported for advanced use cases
from kiota_abstractions.base_request_configuration import RequestConfiguration
from space_gass_api.generated.job.structure.nodes.nodes_request_builder import (
    NodesRequestBuilder,
)

qp = NodesRequestBuilder.NodesRequestBuilderGetQueryParameters(
    node_type=models.NodeTypeFilter.Restrained)
nodes = await client.job.structure.nodes.get(
    request_configuration=RequestConfiguration(query_parameters=qp))
```

Keyword argument names match the **snake_case field names** on the
builder's query parameters (e.g. `node_type`, `limit`, `offset`,
`min_x`). Invalid names raise `TypeError` with a clear message.

## Documentation

- [Getting Started](https://api.spacegass.com/docs/getting-started/quick-start)
- [API Reference](https://api.spacegass.com/docs/api)
- [Examples](https://github.com/Spacegass/space-gass-api/tree/main/sdks/python/examples)
