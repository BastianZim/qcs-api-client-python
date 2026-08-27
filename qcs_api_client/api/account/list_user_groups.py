from typing import Any
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.list_groups_response import ListGroupsResponse
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    user_id: str,
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/groups".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | ListGroupsResponse | None:
    if response.status_code == 200:
        response_200 = ListGroupsResponse.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Error | ListGroupsResponse]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    user_id: str,
    *,
    client: httpx.Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListGroupsResponse]:
    """List QCS groups for the requested user

     List QCS groups for the requested user

    Args:
        user_id (str):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListGroupsResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        user_id=user_id,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    user_id: str,
    *,
    client: httpx.Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListGroupsResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    user_id: str,
    *,
    client: httpx.AsyncClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListGroupsResponse]:
    """List QCS groups for the requested user

     List QCS groups for the requested user

    Args:
        user_id (str):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListGroupsResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        user_id=user_id,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    user_id: str,
    *,
    client: httpx.AsyncClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListGroupsResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
