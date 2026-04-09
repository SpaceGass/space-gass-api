"""
Convenience factory for creating a ready-to-use SpaceGassApiClient.
"""

from kiota_abstractions.authentication import AnonymousAuthenticationProvider
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from space_gass_api.space_gass_api_client import SpaceGassApiClient

DEFAULT_BASE_URL = "http://localhost:5000/api/v1"


def create_client(base_url: str = DEFAULT_BASE_URL) -> SpaceGassApiClient:
    """
    Create a SpaceGassApiClient with default settings.

    Args:
        base_url: Base URL of the SPACE GASS API.
                  Defaults to http://localhost:5000/api/v1.

    Returns:
        A configured client ready to make API calls.
    """
    adapter = HttpxRequestAdapter(AnonymousAuthenticationProvider())
    adapter.base_url = base_url
    return SpaceGassApiClient(adapter)


# Attach as a static method on the client class for convenience:
#   client = SpaceGassApiClient.create_client()
SpaceGassApiClient.create_client = staticmethod(create_client)
