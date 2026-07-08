from space_gass_api import SpaceGassApiClient


def test_default_base_url_appends_api_path():
    client = SpaceGassApiClient.create_client()
    assert client.request_adapter.base_url == "http://localhost:34560/api/v1"


def test_custom_base_url_trims_trailing_slash():
    client = SpaceGassApiClient.create_client("https://localhost:53484/")
    assert client.request_adapter.base_url == "https://localhost:53484/api/v1"
