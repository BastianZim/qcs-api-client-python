from typing import Any

import httpx
from tenacity import retry

from ...models.list_endpoints_response import ListEndpointsResponse
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
    page_size: int | Unset = 10,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/endpoints",
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> ListEndpointsResponse | ValidationError | None:
    if response.status_code == 200:
        response_200 = ListEndpointsResponse.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[ListEndpointsResponse | ValidationError]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    filter_: str | Unset = UNSET,
    page_size: int | Unset = 10,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[ListEndpointsResponse | ValidationError]:
    """List Endpoints

     List all endpoints, optionally filtering by attribute.

    Args:
        filter_ (str | Unset): Filtering logic specified using [rule-
            engine](https://zerosteiner.github.io/rule-engine/syntax.html) grammar
        page_size (int | Unset):  Default: 10.
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListEndpointsResponse | ValidationError]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        filter_=filter_,
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
    *,
    client: httpx.Client,
    filter_: str | Unset = UNSET,
    page_size: int | Unset = 10,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[ListEndpointsResponse | ValidationError]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
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
    *,
    client: httpx.AsyncClient,
    filter_: str | Unset = UNSET,
    page_size: int | Unset = 10,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[ListEndpointsResponse | ValidationError]:
    """List Endpoints

     List all endpoints, optionally filtering by attribute.

    Args:
        filter_ (str | Unset): Filtering logic specified using [rule-
            engine](https://zerosteiner.github.io/rule-engine/syntax.html) grammar
        page_size (int | Unset):  Default: 10.
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListEndpointsResponse | ValidationError]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        filter_=filter_,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    filter_: str | Unset = UNSET,
    page_size: int | Unset = 10,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[ListEndpointsResponse | ValidationError]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
