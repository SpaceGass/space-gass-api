"""
Auto-generated post-Kiota by `tools/regen_python_inits.py` — DO NOT EDIT.

Imports the generated `SpaceGassApiClient`, attaches the
`create_client` factory and re-exports the `query` helper from the
hand-maintained `space_gass_api_extensions` module.

Usage:

    from space_gass_api import SpaceGassApiClient, query
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()
    node = await client.job.structure.nodes.post(models.NodeCreate(x=0, y=0, z=0))
    restrained = await query(client.job.structure.nodes,
                             node_type=models.NodeTypeFilter.Restrained)
"""

from .space_gass_api_client import SpaceGassApiClient
from space_gass_api_extensions import create_client, query

SpaceGassApiClient.create_client = staticmethod(create_client)

__all__ = ["SpaceGassApiClient", "query"]
