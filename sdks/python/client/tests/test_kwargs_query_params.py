"""The kwargs query-parameter enhancement on get/post/patch/delete.

Every builder verb with a matching ``{Verb}QueryParameters`` dataclass
accepts those parameters as keyword arguments (see
``_enhance_request_methods`` in ``space_gass_api_client.py``).
"""

import pytest
from kiota_abstractions.base_request_configuration import RequestConfiguration

import space_gass_api.models as models


async def test_get_kwargs_add_query_param(client, recorded):
    await client.job.structure.nodes.get(node_type=models.NodeTypeFilter.Restrained)

    assert recorded.last.method == "GET"
    assert "nodeType=" in str(recorded.last.url)


async def test_bulk_post_kwargs_add_query_param(client, recorded):
    await client.job.structure.nodes.bulk.post(
        [models.NodeCreate(x=1.5)], continue_on_error=True
    )

    assert recorded.last.method == "POST"
    assert "continueOnError=true" in str(recorded.last.url)
    assert '"x": 1.5' in recorded.last_body


async def test_bulk_post_plain_call_has_no_query_string(client, recorded):
    await client.job.structure.nodes.bulk.post([models.NodeCreate(x=1.0)])

    assert recorded.last.url.query == b""


async def test_bulk_post_body_as_keyword_still_routes_to_body(client, recorded):
    await client.job.structure.nodes.bulk.post(
        body=[models.NodeCreate(x=9.0)], continue_on_error=True
    )

    assert '"x": 9.0' in recorded.last_body
    assert "continueOnError=true" in str(recorded.last.url)


async def test_bulk_patch_kwargs_add_query_param(client, recorded):
    await client.job.structure.nodes.bulk.patch(
        [models.NodeUpdate(id=1)], continue_on_error=True
    )

    assert recorded.last.method == "PATCH"
    assert "continueOnError=true" in str(recorded.last.url)


async def test_bulk_delete_kwargs_add_query_param(client, recorded):
    await client.job.structure.nodes.bulk.delete([1, 2, 3], continue_on_error=True)

    assert recorded.last.method == "DELETE"
    assert "continueOnError=true" in str(recorded.last.url)
    assert recorded.last_body.replace(" ", "") == "[1,2,3]"


async def test_bodyless_delete_kwargs_add_query_param(client, recorded):
    await client.job.data.delete(force=True)

    assert recorded.last.method == "DELETE"
    assert "force=true" in str(recorded.last.url)


async def test_request_configuration_path_still_works(client, recorded):
    bulk = client.job.structure.nodes.bulk
    qp = type(bulk).BulkRequestBuilderPostQueryParameters(continue_on_error=True)

    await bulk.post(
        [models.NodeCreate(x=1.0)],
        request_configuration=RequestConfiguration(query_parameters=qp),
    )

    assert "continueOnError=true" in str(recorded.last.url)


async def test_unknown_kwarg_raises_type_error(client):
    with pytest.raises(TypeError):
        await client.job.structure.nodes.bulk.post(
            [models.NodeCreate(x=1.0)], not_a_param=True
        )


async def test_request_configuration_plus_kwargs_raises_type_error(client):
    bulk = client.job.structure.nodes.bulk
    qp = type(bulk).BulkRequestBuilderPostQueryParameters(continue_on_error=True)

    with pytest.raises(TypeError, match="Cannot pass both"):
        await bulk.post(
            [models.NodeCreate(x=1.0)],
            request_configuration=RequestConfiguration(query_parameters=qp),
            continue_on_error=True,
        )


async def test_missing_body_raises_type_error(client):
    with pytest.raises(TypeError):
        await client.job.structure.nodes.bulk.post(continue_on_error=True)
