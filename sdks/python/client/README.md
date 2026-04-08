# space-gass-api

Official Python SDK for the SPACE GASS structural analysis API.

## Quick Start

```python
from extensions.client_extensions import create_client
from space_gass_api.models.node_create import NodeCreate

client = create_client()

# Create a new project
await client.job.new.post()

# Add a node
node = await client.job.structure.nodes.post(
    NodeCreate(x=0, y=0, z=0))

# Close the project
await client.job.close.post()
```

## Documentation

- [Getting Started](https://spacegass.github.io/space-gass-api/)
- [API Reference](https://spacegass.github.io/space-gass-api/api)
- [Examples](https://github.com/Spacegass/space-gass-api/tree/develop/sdks/python/examples)
