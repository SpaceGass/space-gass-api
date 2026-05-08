"""
Hand-maintained companion module for the Kiota-generated SpaceGassApiClient.

Lives at the root of the Python client tree (next to space_gass_api/) so
Kiota's `--clean-output` regen never touches it.

Defines `create_client(...)`. The factory is attached to
`SpaceGassApiClient` as a static method by the post-regen
`space_gass_api/__init__.py` — you don't need to import this module
directly. The public entry point is:

    from space_gass_api import SpaceGassApiClient
    client = SpaceGassApiClient.create_client()
"""

from kiota_abstractions.authentication import AnonymousAuthenticationProvider
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

DEFAULT_BASE_URL = "http://localhost:34560/api/v1"


def create_client(base_url: str = DEFAULT_BASE_URL):
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
