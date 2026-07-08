"""
Hand-maintained client for the SPACE GASS API.

Extends the Kiota-generated ``BaseSpaceGassApiClient`` with a
``create_client()`` factory and the keyword-query-parameter enhancement
on ``get``/``post``/``patch``/``put``/``delete``.

Lives inside the ``space_gass_api`` package but outside the
``generated/`` folder, so Kiota's ``--clean-output`` never touches it.

Usage:

    from space_gass_api import SpaceGassApiClient
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()

    # GET with keyword query parameters
    restrained = await client.job.structure.nodes.get(
        node_type=models.NodeTypeFilter.Restrained)

    reactions = await client.job.query.analysis.static.node_reactions.get(
        cases="1,3-7", nodes="10-12")

    # POST/PATCH/DELETE with keyword query parameters
    result = await client.job.structure.nodes.bulk.post(
        bodies, continue_on_error=True)
"""

from __future__ import annotations

import httpx
from kiota_abstractions.authentication import AnonymousAuthenticationProvider
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_http.httpx_request_adapter import HttpxRequestAdapter, KiotaClientFactory
from kiota_http.middleware.options.redirect_handler_option import RedirectHandlerOption

from .generated.base_space_gass_api_client import BaseSpaceGassApiClient

API_PATH = "/api/v1"
DEFAULT_BASE_URL = "http://localhost:34560"


class SpaceGassApiClient(BaseSpaceGassApiClient):
    """SPACE GASS API client.

    Extends the Kiota-generated ``BaseSpaceGassApiClient`` with a convenience
    factory. Use ``SpaceGassApiClient.create_client()`` to get a fully
    configured instance.
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
            client=httpx.AsyncClient(verify=False, timeout=httpx.Timeout(1800)),
            options=options,
        )

        adapter = HttpxRequestAdapter(
            AnonymousAuthenticationProvider(),
            http_client=http_client,
        )
        adapter.base_url = base_url.rstrip("/") + API_PATH
        return SpaceGassApiClient(adapter)


def _enhance_request_methods():
    """Patch ``BaseRequestBuilder.__init_subclass__`` so every Kiota builder
    whose class body contains a ``{ClassName}{Verb}QueryParameters`` dataclass
    gets that verb method (``get``/``post``/``patch``/``put``/``delete``)
    wrapped to accept keyword query parameters directly.

    Must be called **once**, before any builder module is imported.  The
    auto-generated ``space_gass_api/__init__.py`` takes care of this.
    """
    from kiota_abstractions.base_request_builder import BaseRequestBuilder
    from kiota_abstractions.base_request_configuration import RequestConfiguration
    import functools
    import inspect

    if getattr(BaseRequestBuilder, "_request_methods_enhanced", False):
        return

    def _wrap(original, qp_class, label):
        # Kiota emits `post(self, body, request_configuration=None)` when the
        # endpoint has a request body and drops `body` when it doesn't, so the
        # wrapper has to mirror whichever shape it is given.
        has_body = "body" in inspect.signature(original).parameters

        def _config_from(params, request_configuration):
            if not params:
                return request_configuration
            if request_configuration is not None:
                raise TypeError(
                    f"Cannot pass both request_configuration and "
                    f"keyword query parameters to {label}."
                )
            return RequestConfiguration(query_parameters=qp_class(**params))

        if has_body:

            @functools.wraps(original)
            async def enhanced(self, body, request_configuration=None, **params):
                return await original(
                    self,
                    body,
                    request_configuration=_config_from(params, request_configuration),
                )

        else:

            @functools.wraps(original)
            async def enhanced(self, request_configuration=None, **params):
                return await original(
                    self,
                    request_configuration=_config_from(params, request_configuration),
                )

        return enhanced

    def _init_subclass(cls, **kwargs):
        for verb in ("get", "post", "patch", "put", "delete"):
            qp_class = cls.__dict__.get(
                f"{cls.__name__}{verb.capitalize()}QueryParameters"
            )
            original = cls.__dict__.get(verb)
            if qp_class is None or original is None:
                continue
            setattr(
                cls,
                verb,
                _wrap(original, qp_class, f"{cls.__name__}.{verb}()"),
            )

    BaseRequestBuilder.__init_subclass__ = classmethod(_init_subclass)
    BaseRequestBuilder._request_methods_enhanced = True
