"""
Hand-maintained companion module for the Kiota-generated SpaceGassApiClient.

Lives at the root of the Python client tree (next to space_gass_api/) so
Kiota's `--clean-output` regen never touches it.

Defines two helpers:

- ``create_client(...)`` — attached to ``SpaceGassApiClient`` as a static
  method by the post-regen ``space_gass_api/__init__.py``.

- ``_query_method`` — attached to ``BaseRequestBuilder`` as an instance
  method named ``.query()`` by the post-regen
  ``space_gass_api/__init__.py``. Lets every kiota builder accept GET
  query parameters as keyword arguments, instead of forcing callers to
  hand-import the deeply-nested ``{Builder}GetQueryParameters`` class.

Public API:

    from space_gass_api import SpaceGassApiClient
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()

    # GET with query params — same fluent shape as .get() / .post() / .patch()
    restrained = await client.job.structure.nodes.query(
        node_type=models.NodeTypeFilter.Restrained)

    reactions = await client.job.query.analysis.static.node_reactions.query(
        cases="1,3-7", nodes="10-12")
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


async def _query_method(self, **params):
    """Run a GET against this builder with kwargs as query parameters.

    Replaces the verbose pattern:

        from kiota_abstractions.base_request_configuration import RequestConfiguration
        from space_gass_api.job.structure.nodes.nodes_request_builder import NodesRequestBuilder

        qp = NodesRequestBuilder.NodesRequestBuilderGetQueryParameters(
            node_type=models.NodeTypeFilter.Restrained)
        nodes = await client.job.structure.nodes.get(
            request_configuration=RequestConfiguration(query_parameters=qp))

    with the fluent:

        nodes = await client.job.structure.nodes.query(
            node_type=models.NodeTypeFilter.Restrained)

    Works because kiota generates a nested
    ``{BuilderName}GetQueryParameters`` dataclass on every builder that
    accepts GET query parameters; this method finds it by name and
    builds the request configuration for you.

    Attached to ``kiota_abstractions.base_request_builder.BaseRequestBuilder``
    by the auto-generated ``space_gass_api/__init__.py`` so every builder
    inherits it without per-class registration.

    Parameters
    ----------
    **params:
        Keyword arguments forwarded to the dataclass constructor — must
        match its field names (snake_case in Python).

    Raises
    ------
    TypeError
        If this builder has no nested GetQueryParameters class (i.e. it
        doesn't accept GET query parameters).
    """
    # Lazy import — same reason as create_client.
    from kiota_abstractions.base_request_configuration import RequestConfiguration

    qp_class_name = f"{type(self).__name__}GetQueryParameters"
    qp_class = getattr(type(self), qp_class_name, None)
    if qp_class is None:
        raise TypeError(
            f"{type(self).__name__} has no nested {qp_class_name} class — "
            "this builder does not accept GET query parameters."
        )
    qp = qp_class(**params)
    return await self.get(
        request_configuration=RequestConfiguration(query_parameters=qp)
    )
