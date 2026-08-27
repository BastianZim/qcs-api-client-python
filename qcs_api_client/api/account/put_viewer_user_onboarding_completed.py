from typing import Any

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.viewer_user_onboarding_completed import ViewerUserOnboardingCompleted
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    *,
    body: ViewerUserOnboardingCompleted | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/viewer/onboardingCompleted",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | ViewerUserOnboardingCompleted | None:
    if response.status_code == 200:
        response_200 = ViewerUserOnboardingCompleted.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Error | ViewerUserOnboardingCompleted]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    body: ViewerUserOnboardingCompleted | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ViewerUserOnboardingCompleted]:
    """Update the onboarding status of the authenticated user.

    Args:
        body (ViewerUserOnboardingCompleted | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ViewerUserOnboardingCompleted]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    *,
    client: httpx.Client,
    body: dict,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ViewerUserOnboardingCompleted]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    *,
    client: httpx.AsyncClient,
    body: ViewerUserOnboardingCompleted | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ViewerUserOnboardingCompleted]:
    """Update the onboarding status of the authenticated user.

    Args:
        body (ViewerUserOnboardingCompleted | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ViewerUserOnboardingCompleted]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    body: dict,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ViewerUserOnboardingCompleted]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
