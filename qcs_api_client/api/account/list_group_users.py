from typing import Any
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.list_group_users_response import ListGroupUsersResponse
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    group_name: str,
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
        "url": "/v1/groups/{group_name}/users".format(
            group_name=quote(str(group_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | ListGroupUsersResponse | None:
    if response.status_code == 200:
        response_200 = ListGroupUsersResponse.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Error | ListGroupUsersResponse]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    group_name: str,
    *,
    client: httpx.Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListGroupUsersResponse]:
    """List users belonging to a group

     List users belonging to a group. Note, group membership may take several minutes to update within
    our identity provider. After adding or removing a user to or from a group, please allow up to 60
    minutes for changes to be reflected.

    Args:
        group_name (str):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListGroupUsersResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
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
    group_name: str,
    *,
    client: httpx.Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListGroupUsersResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
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
    group_name: str,
    *,
    client: httpx.AsyncClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListGroupUsersResponse]:
    """List users belonging to a group

     List users belonging to a group. Note, group membership may take several minutes to update within
    our identity provider. After adding or removing a user to or from a group, please allow up to 60
    minutes for changes to be reflected.

    Args:
        group_name (str):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListGroupUsersResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        group_name=group_name,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    group_name: str,
    *,
    client: httpx.AsyncClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListGroupUsersResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
