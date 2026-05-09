"""
Hand-maintained companion module for the Kiota-generated SpaceGassApiClient.

Lives at the root of the Python client tree (next to space_gass_api/) so
Kiota's `--clean-output` regen never touches it.

Defines two helpers:

- ``create_client(...)`` — attached to ``SpaceGassApiClient`` as a static
  method by the post-regen ``space_gass_api/__init__.py``.

- ``_enhance_get_methods()`` — called once at package init to patch
  ``BaseRequestBuilder.__init_subclass__``. Every Kiota builder that has
  a nested ``{ClassName}GetQueryParameters`` dataclass gets its ``.get()``
  method wrapped so callers can pass query parameters as keyword arguments.

Public API:

    from space_gass_api import SpaceGassApiClient
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()

    # GET with keyword query parameters
    restrained = await client.job.structure.nodes.get(
        node_type=models.NodeTypeFilter.Restrained)

    reactions = await client.job.query.analysis.static.node_reactions.get(
        cases="1,3-7", nodes="10-12")
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from kiota_abstractions.authentication import AnonymousAuthenticationProvider
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

if TYPE_CHECKING:
    from space_gass_api.space_gass_api_client import SpaceGassApiClient

DEFAULT_BASE_URL = "http://localhost:34560/api/v1"


def create_client(base_url: str = DEFAULT_BASE_URL) -> SpaceGassApiClient:
    """Create a SpaceGassApiClient bound to the local SPACE GASS API service.

    Parameters
    ----------
    base_url:
        Base URL of the SPACE GASS API. Defaults to
        ``http://localhost:34560/api/v1``. Override only if the service
        is running on a non-default port.

    Returns
    -------
    A configured `SpaceGassApiClient` ready to make API calls.
    """
    # Lazy import to avoid a circular load when this module is imported
    # from the auto-generated `space_gass_api/__init__.py` at package init.
    from space_gass_api.space_gass_api_client import SpaceGassApiClient

    adapter = HttpxRequestAdapter(AnonymousAuthenticationProvider())
    adapter.base_url = base_url
    return SpaceGassApiClient(adapter)


def _enhance_get_methods():
    """Patch ``BaseRequestBuilder.__init_subclass__`` so every Kiota builder
    whose class body contains a ``{ClassName}GetQueryParameters`` dataclass
    gets its ``.get()`` wrapped to accept keyword arguments directly.

    Must be called **once**, before any builder module is imported.  The
    auto-generated ``space_gass_api/__init__.py`` takes care of this.
    """
    from kiota_abstractions.base_request_builder import BaseRequestBuilder
    from kiota_abstractions.base_request_configuration import RequestConfiguration
    import functools

    if getattr(BaseRequestBuilder, "_get_enhanced", False):
        return

    def _init_subclass(cls, **kwargs):
        qp_name = f"{cls.__name__}GetQueryParameters"
        qp_class = cls.__dict__.get(qp_name)

        if qp_class is not None and "get" in cls.__dict__:
            original_get = cls.__dict__["get"]

            @functools.wraps(original_get)
            async def enhanced_get(self, request_configuration=None, **params):
                if params:
                    if request_configuration is not None:
                        raise TypeError(
                            f"Cannot pass both request_configuration and "
                            f"keyword query parameters to "
                            f"{type(self).__name__}.get()."
                        )
                    qp = qp_class(**params)
                    request_configuration = RequestConfiguration(
                        query_parameters=qp
                    )
                return await original_get(
                    self, request_configuration=request_configuration
                )

            cls.get = enhanced_get

    BaseRequestBuilder.__init_subclass__ = classmethod(_init_subclass)
    BaseRequestBuilder._get_enhanced = True
