"""
Auto-generated post-Kiota by `tools/regen_python_inits.py` — DO NOT EDIT.

Imports the generated `SpaceGassApiClient`, attaches the
`create_client` factory from the hand-maintained
`space_gass_api_extensions` module, and re-exports the client.

Usage:

    from space_gass_api import SpaceGassApiClient
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()
    node = await client.job.structure.nodes.post(models.NodeCreate(x=0, y=0, z=0))
"""

from .space_gass_api_client import SpaceGassApiClient
from space_gass_api_extensions import create_client

SpaceGassApiClient.create_client = staticmethod(create_client)

__all__ = ["SpaceGassApiClient"]
