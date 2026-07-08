"""The ``space_gass_api.models`` re-export shim (written post-Kiota by
``tools/regen_python_inits.py``)."""

import importlib

import pytest
from kiota_abstractions.api_error import APIError


def test_documented_model_imports_resolve():
    from space_gass_api.models import (  # noqa: F401
        ErrorResponse,
        NodeCreate,
        OpenJobRequest,
        OpenSampleRequest,
        SaveJobRequest,
    )


def test_error_response_is_catchable_api_error():
    from space_gass_api.models import ErrorResponse

    assert issubclass(ErrorResponse, APIError)


def test_models_module_attribute_access():
    import space_gass_api.models as models

    assert models.NodeCreate(x=1.0).x == 1.0


def test_models_submodule_imports_do_not_exist():
    # Regression for a docs bug: models is a flat re-export shim, so
    # `space_gass_api.models.error_response` must not be documented or used.
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("space_gass_api.models.error_response")


async def test_error_body_surfaces_as_typed_exception(make_client):
    import httpx

    from space_gass_api.models import ErrorResponse

    client = make_client(
        lambda request: httpx.Response(
            404,
            json={
                "title": "Not Found",
                "status": 404,
                "detail": "Node 999 not found",
                "errorCode": "NOT_FOUND",
            },
        )
    )

    with pytest.raises(ErrorResponse) as excinfo:
        await client.job.structure.nodes.by_id(999).get()

    assert excinfo.value.status == 404
    assert excinfo.value.detail == "Node 999 not found"
    assert excinfo.value.error_code == "NOT_FOUND"
