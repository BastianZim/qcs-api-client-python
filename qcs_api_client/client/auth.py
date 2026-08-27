from http import HTTPStatus

import httpx
from pydantic import BaseModel, Field
from qcs_api_client_common.configuration import ClientConfiguration, SecretAccessToken


class QCSAuthConfiguration(BaseModel):
    """This configures how ``QCSAuth`` implements its access token refresh mechanism."""

    pre: bool = False
    """Pre-emptively refresh access tokens.

    When set to True, this will refresh the token before setting the outgoing Authorization header.
    """

    post: bool = True
    """Refresh access tokens based on response status code.

    When set to True, this will check responses for the status codes configured
    in ``post_refresh_statuses``. On match, ``QCSAuth`` will refresh the access token
    and retry the request.
    """

    post_refresh_statuses: set[int] = Field(default_factory=lambda: {HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN})
    """Response status codes which indicates a possible expired token payload.

    This contains a set of HTTP status codes which ``QCSAuth`` will check on
    responses when `post` is set to True.
    """


class QCSAuth(httpx.Auth):
    """Implements ``httpx.Auth`` ``sync_auth_flow`` and ``async_auth_flow``.

    Access tokens are refreshed via OAuth2 refresh mechanism as indicated
    by ``QCSAuthConfiguration``.
    """

    def __init__(
        self,
        client_configuration: ClientConfiguration,
        auth_configuration: QCSAuthConfiguration = None,
    ):
        self._client_configuration = client_configuration
        self._auth_configuration = auth_configuration or QCSAuthConfiguration()

    def get_access_token(self) -> SecretAccessToken:
        """Return an access token, possibly updating a refresh token as a side-effect."""
        return self._client_configuration.get_bearer_access_token()

    async def get_access_token_async(self) -> SecretAccessToken:
        """Return an access token, possibly updating a refresh token as a side-effect."""
        return await self._client_configuration.get_bearer_access_token_async()

    def sync_auth_flow(self, request):
        if self._auth_configuration.pre:
            token = self.get_access_token().secret
            request.headers["Authorization"] = f"Bearer {token}"

        response = yield request

        if self._auth_configuration.post and response.status_code in self._auth_configuration.post_refresh_statuses:
            token = self.get_access_token().secret
            request.headers["Authorization"] = f"Bearer {token}"
            yield request

    async def async_auth_flow(self, request):
        if self._auth_configuration.pre:
            token = (await self.get_access_token_async()).secret
            request.headers["Authorization"] = f"Bearer {token}"

        response = yield request

        if self._auth_configuration.post and response.status_code in self._auth_configuration.post_refresh_statuses:
            token = (await self.get_access_token_async()).secret
            request.headers["Authorization"] = f"Bearer {token}"
            yield request
