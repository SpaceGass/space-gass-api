"""Shared fixtures: a ``SpaceGassApiClient`` wired to ``httpx.MockTransport``.

The transport records every outgoing request and answers with canned JSON,
so tests can assert what actually goes on the wire — URLs, query strings,
verbs, serialized bodies — without a live SPACE GASS service.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Allow running straight from the repo without installing the package.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import httpx
import pytest
from kiota_abstractions.authentication import AnonymousAuthenticationProvider
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from space_gass_api import SpaceGassApiClient


class RecordedRequests:
    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []

    @property
    def last(self) -> httpx.Request:
        return self.requests[-1]

    @property
    def last_body(self) -> str:
        return self.last.content.decode()


@pytest.fixture
def recorded() -> RecordedRequests:
    return RecordedRequests()


@pytest.fixture
def make_client(recorded):
    """Factory for a client with a custom response handler."""

    def factory(respond=None) -> SpaceGassApiClient:
        def handler(request: httpx.Request) -> httpx.Response:
            recorded.requests.append(request)
            if respond is not None:
                return respond(request)
            if request.method == "GET" and request.url.path.endswith("/structure/nodes"):
                return httpx.Response(200, json=[])
            return httpx.Response(200, json={})

        adapter = HttpxRequestAdapter(
            AnonymousAuthenticationProvider(),
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        adapter.base_url = "http://localhost:34560/api/v1"
        return SpaceGassApiClient(adapter)

    return factory


@pytest.fixture
def client(make_client) -> SpaceGassApiClient:
    return make_client()
