from typing import Any

import httpx
from tenacity import retry

from ...models.announcements_response import AnnouncementsResponse
from ...models.error import Error
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    include_dismissed: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["includeDismissed"] = include_dismissed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/viewer/announcements",
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> AnnouncementsResponse | Error | None:
    if response.status_code == 200:
        response_200 = AnnouncementsResponse.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[AnnouncementsResponse | Error]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    include_dismissed: bool | Unset = False,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[AnnouncementsResponse | Error]:
    """List all announcements relevant to the authenticating user. By default, does not include dismissed
    announcements.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        include_dismissed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnouncementsResponse | Error]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        include_dismissed=include_dismissed,
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
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    include_dismissed: bool | Unset = False,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[AnnouncementsResponse | Error]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
        include_dismissed=include_dismissed,
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
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    include_dismissed: bool | Unset = False,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[AnnouncementsResponse | Error]:
    """List all announcements relevant to the authenticating user. By default, does not include dismissed
    announcements.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        include_dismissed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnouncementsResponse | Error]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        include_dismissed=include_dismissed,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    include_dismissed: bool | Unset = False,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[AnnouncementsResponse | Error]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
        include_dismissed=include_dismissed,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
