"""
Auto-generated post-Kiota by `tools/regen_python_inits.py` — DO NOT EDIT.

Wires up the hand-maintained extensions on top of the Kiota-generated
client:

- ``create_client(...)`` is attached as a static method on
  ``SpaceGassApiClient`` so callers can write
  ``SpaceGassApiClient.create_client()``.

- ``query(...)`` is attached as an instance method on every kiota
  request builder (via ``BaseRequestBuilder``) so callers can pass GET
  query parameters as kwargs in the same fluent style as
  ``.get()`` / ``.post()`` / ``.patch()``.

Usage:

    from space_gass_api import SpaceGassApiClient
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()
    node = await client.job.structure.nodes.post(models.NodeCreate(x=0, y=0, z=0))
    restrained = await client.job.structure.nodes.query(
        node_type=models.NodeTypeFilter.Restrained)
"""

from kiota_abstractions.base_request_builder import BaseRequestBuilder

from .space_gass_api_client import SpaceGassApiClient
from space_gass_api_extensions import create_client, _query_method

SpaceGassApiClient.create_client = staticmethod(create_client)
BaseRequestBuilder.query = _query_method

__all__ = ["SpaceGassApiClient"]
