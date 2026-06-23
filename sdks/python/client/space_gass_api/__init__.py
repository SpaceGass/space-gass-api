"""
Auto-generated post-Kiota by `tools/regen_python_inits.py` — DO NOT EDIT.

Wires up the hand-maintained extensions on top of the Kiota-generated
client:

- ``SpaceGassApiClient`` extends the generated ``BaseApiClient``
  with the ``create_client()`` factory method.

- ``.get(**kwargs)`` is auto-enhanced on every builder that has GET
  query parameters, so callers can pass filters as keyword arguments
  directly instead of constructing ``RequestConfiguration`` objects.

Usage:

    from space_gass_api import SpaceGassApiClient
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()
    node = await client.job.structure.nodes.post(models.NodeCreate(x=0, y=0, z=0))
    restrained = await client.job.structure.nodes.get(
        node_type=models.NodeTypeFilter.Restrained)
"""

from .space_gass_api_client import _enhance_get_methods

_enhance_get_methods()

from .space_gass_api_client import SpaceGassApiClient
from .upload_requests import ImportTxtRequest, NewFromTemplateRequest

__all__ = ["ImportTxtRequest", "NewFromTemplateRequest", "SpaceGassApiClient"]
