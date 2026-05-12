"""
Hand-maintained client for the SPACE GASS API.

Extends the Kiota-generated ``BaseSpaceGassApiClient`` with a
``create_client()`` factory and the ``.get(**kwargs)`` enhancement.

Lives at the root of the Python client tree (next to space_gass_api/) so
Kiota's ``--clean-output`` regen never touches it.

Usage:

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

import httpx
from kiota_abstractions.authentication import AnonymousAuthenticationProvider
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_http.httpx_request_adapter import HttpxRequestAdapter, KiotaClientFactory
from kiota_http.middleware.options.redirect_handler_option import RedirectHandlerOption

from space_gass_api.base_space_gass_api_client import BaseSpaceGassApiClient

API_PATH = "/api/v1"
DEFAULT_BASE_URL = "http://localhost:34560"


class SpaceGassApiClient(BaseSpaceGassApiClient):
    """SPACE GASS API client.

    Extends the Kiota-generated ``BaseSpaceGassApiClient`` with a
    convenience factory. Use ``SpaceGassApiClient.create_client()`` to
    get a fully configured instance.
    """

    def __init__(self, request_adapter: RequestAdapter) -> None:
        super().__init__(request_adapter)

    @staticmethod
    def create_client(base_url: str = DEFAULT_BASE_URL) -> SpaceGassApiClient:
        """Create a SpaceGassApiClient bound to the local SPACE GASS API.

        Parameters
        ----------
        base_url:
            Root URL of the SPACE GASS API (without ``/api/v1``).
            Defaults to ``http://localhost:34560``. Override only if the
            service is running on a non-default port. Use ``https://``
            for HTTPS connections (e.g. ``https://localhost:53484``).

        Returns
        -------
        A configured ``SpaceGassApiClient`` ready to make API calls.

        Notes
        -----
        The API may serve HTTPS with a self-signed certificate, so SSL
        verification is disabled by default.  HTTP-to-HTTPS redirects
        are also allowed so either scheme works for the same port.
        """
        # Allow HTTP ↔ HTTPS redirects (the local API may redirect).
        options = {
            RedirectHandlerOption.REDIRECT_HANDLER_OPTION_KEY: RedirectHandlerOption(
                allow_redirect_on_scheme_change=True,
            ),
        }
        # Disable SSL verification for the self-signed certificate the
        # local SPACE GASS API uses.
        http_client = KiotaClientFactory.create_with_default_middleware(
            client=httpx.AsyncClient(verify=False),
            options=options,
        )

        adapter = HttpxRequestAdapter(
            AnonymousAuthenticationProvider(),
            http_client=http_client,
        )
        adapter.base_url = base_url.rstrip("/") + API_PATH
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
