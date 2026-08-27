import pytest
import respx
from httpx import Request, Response

from qcs_api_client.client import ClientConfiguration, build_async_client, build_sync_client
from qcs_api_client.models.health import Health
from qcs_api_client.operations.asyncio import get_health as asyncio_get_health
from qcs_api_client.operations.sync import get_health


@pytest.mark.respx(assert_all_mocked=True)
class TestSyncClient:
    def test_adds_header(self, client_configuration: ClientConfiguration, respx_mock: respx.MockRouter):
        """Assert that a sync client can be constructed and make a call with authorization header."""

        with build_sync_client(configuration=client_configuration) as client:
            target_route = respx_mock.get(client_configuration.api_url).mock(side_effect=[Response(401), Response(200)])
            response = client.get(client_configuration.api_url)
            assert target_route.called
            assert response.status_code == 200
            access_token = client_configuration.get_bearer_access_token().secret
            assert response.request.headers.get("Authorization") == f"Bearer {access_token}"

    def test_no_header_needed(self, client_configuration: ClientConfiguration, respx_mock: respx.MockRouter):
        """Assert that a generated request function can be called with a sync client."""

        def assert_request(request: Request):
            assert request.headers.get("Authorization") is None
            assert request.headers.get("foo") == "bar"
            return Response(200, json=dict(status="PASS"))

        respx_mock.get(client_configuration.api_url).mock(side_effect=assert_request)
        with build_sync_client(configuration=client_configuration) as client:
            response = get_health(client=client, httpx_request_kwargs={"headers": {"foo": "bar"}})
            assert response.status_code == 200
            assert response.parsed == Health(status="PASS")


@pytest.mark.asyncio
@pytest.mark.respx(assert_all_mocked=True)
class TestAsyncClient:
    async def test_adds_header(self, client_configuration: ClientConfiguration, respx_mock: respx.MockRouter):
        """Assert that an async client can be constructed and make a call with authorization header."""

        async with build_async_client(configuration=client_configuration) as client:
            target_route = respx_mock.get(client_configuration.api_url).mock(side_effect=[Response(401), Response(200)])
            response = await client.get(client_configuration.api_url)
            assert target_route.called
            assert response.status_code == 200
            access_token = (await client_configuration.get_bearer_access_token_async()).secret
            assert response.request.headers.get("Authorization") == f"Bearer {access_token}"

    async def test_no_header(self, client_configuration: ClientConfiguration, respx_mock: respx.MockRouter):
        """Assert that the client makes async requests without authentication if configuration is empty."""

        def assert_request(request: Request):
            assert request.headers.get("Authorization") is None
            assert request.headers.get("foo") == "bar"
            return Response(200, json=dict(status="PASS"))

        respx_mock.get(client_configuration.api_url).mock(side_effect=assert_request)
        async with build_async_client(configuration=client_configuration) as client:
            response = await asyncio_get_health(client=client, httpx_request_kwargs={"headers": {"foo": "bar"}})
            assert response.status_code == 200
            assert response.parsed == Health(status="PASS")
