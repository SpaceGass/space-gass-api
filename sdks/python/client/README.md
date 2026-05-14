# space-gass-api

Official Python SDK for the SPACE GASS structural analysis API.

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
Passing both keyword arguments and `request_configuration` at the same
time raises `TypeError`.

The keyword argument names match the **snake_case field names** on the
builder's `GetQueryParameters` dataclass (e.g. `node_type`, `limit`,
`offset`, `min_x`). Invalid names raise `TypeError` from the dataclass
constructor with a clear message.

### Which builders are enhanced?

Only builders whose class body contains a nested
`{ClassName}GetQueryParameters` dataclass — roughly half of all builders.
Builders without GET query parameters (e.g. `CloseRequestBuilder`,
`NewRequestBuilder`) are untouched; their `.get()` signature is unchanged.

### How it works

The enhancement uses Python's built-in `__init_subclass__` hook
(available since Python 3.6). At package import time:

1. `space_gass_api/__init__.py` calls `_enhance_get_methods()` from the
   hand-maintained `space_gass_api_extensions.py`.

2. This replaces `BaseRequestBuilder.__init_subclass__` with a custom
   version. Python calls this hook automatically whenever a new class
   inherits from `BaseRequestBuilder` — i.e. when each builder class is
   defined.

3. Kiota uses lazy imports: builder modules aren't loaded until you
   access them (e.g. `client.job.structure.nodes`). When a builder
   module is first imported, its class definition triggers
   `__init_subclass__`.

4. The hook inspects the new class. If it finds both a
   `{ClassName}GetQueryParameters` inner class and a `.get()` method, it
   wraps `.get()` with a version that accepts `**kwargs`. The original
   `.get()` is preserved in a closure.

5. The wrapping cost is paid once per builder class (at first import),
   not per call. Subsequent `.get()` calls on any instance go straight
   through the wrapper.

### What you need to maintain

**Nothing changes when Kiota regenerates the SDK.** The enhancement
lives entirely in two hand-maintained files that Kiota's `--clean-output`
never touches:

| File | Purpose |
|------|---------|
| `space_gass_api_extensions.py` | Defines `create_client()` and `_enhance_get_methods()` |
| `tools/regen_python_inits.py` | Writes `__init__.py` with the wiring code after each regen |

After a Kiota regen, run `python tools/regen_python_inits.py` (the CI
workflow does this automatically). The generated `__init__.py` calls
`_enhance_get_methods()` before importing the client, ensuring the hook
is in place before any builder class is defined.

New builders added by future Kiota regens are automatically picked up —
`__init_subclass__` fires for every `BaseRequestBuilder` subclass, no
registration needed.

## Documentation

- [Getting Started](https://api.spacegass.com/docs/)
- [API Reference](https://api.spacegass.com/docs/api)
- [Examples](https://github.com/Spacegass/space-gass-api/tree/develop/sdks/python/examples)
