"""
Shared helper for creating a configured SpaceGass API client.
"""

import httpx
from kiota_abstractions.authentication import ApiKeyAuthenticationProvider, KeyLocation
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from space_gass_api.space_gass_api_client import SpaceGassApiClient

DEFAULT_BASE_URL = "https://localhost:53483/api/v1"
DEFAULT_API_KEY = "local"


def create_client(
    base_url: str = DEFAULT_BASE_URL,
    api_key: str = DEFAULT_API_KEY,
) -> SpaceGassApiClient:
    """
    Create a SpaceGassApiClient configured with API key authentication
    and a development SSL bypass.

    Args:
        base_url: Base URL of the SpaceGass API (default: https://localhost:53483/api/v1).
        api_key: API key for authentication (default: "local").
    """
    auth_provider = ApiKeyAuthenticationProvider(
        api_key=api_key,
        parameter_name="X-API-KEY",
        key_location=KeyLocation.Header,
    )

    # Bypass SSL verification for local development with self-signed certificates.
    http_client = httpx.AsyncClient(verify=False)

    adapter = HttpxRequestAdapter(
        authentication_provider=auth_provider,
        http_client=http_client,
    )
    adapter.base_url = base_url

    return SpaceGassApiClient(adapter)
