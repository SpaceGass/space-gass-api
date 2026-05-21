# space-gass-api

Official Python SDK for the SPACE GASS API.

The SPACE GASS API gives you programmatic access to SPACE GASS structural analysis — open or create new job files, read or edit structural entities, run analyses, and query results.

## Quick Start

```python
from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models

client = SpaceGassApiClient.create_client()

# Create a new project
await client.job.new.post()

# Add a node
node = await client.job.structure.nodes.post(
    models.NodeCreate(x=0, y=0, z=0))

# Query with filters — pass query parameters as keyword arguments
restrained = await client.job.structure.nodes.get(
    node_type=models.NodeTypeFilter.Restrained)

# Close the project
await client.job.close.post()
```

## Enhanced `.get()` with keyword arguments

Kiota-generated builders normally require verbose `RequestConfiguration`
objects to pass GET query parameters:

```python
from kiota_abstractions.base_request_configuration import RequestConfiguration
from space_gass_api.job.structure.nodes.nodes_request_builder import (
    NodesRequestBuilder,
)

qp = NodesRequestBuilder.NodesRequestBuilderGetQueryParameters(
    node_type=models.NodeTypeFilter.Restrained)
nodes = await client.job.structure.nodes.get(
    request_configuration=RequestConfiguration(query_parameters=qp))
```

This SDK enhances `.get()` so you can pass those same parameters as
keyword arguments directly:

```python
nodes = await client.job.structure.nodes.get(
    node_type=models.NodeTypeFilter.Restrained)
```

Both forms are supported — the verbose `request_configuration=` pattern
still works for advanced use cases (custom headers, middleware options).

Keyword argument names match the **snake_case field names** on the
builder's query parameters (e.g. `node_type`, `limit`, `offset`,
`min_x`). Invalid names raise `TypeError` with a clear message.

## Documentation

- [Getting Started](https://api.spacegass.com/docs/)
- [API Reference](https://api.spacegass.com/docs/api)
- [Examples](https://github.com/Spacegass/space-gass-api/tree/main/sdks/python/examples)
