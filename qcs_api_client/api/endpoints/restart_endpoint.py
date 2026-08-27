from typing import Any, cast
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.restart_endpoint_request import RestartEndpointRequest
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    endpoint_id: str,
    *,
    body: RestartEndpointRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/endpoints/{endpoint_id}:restart".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, response: httpx.Response) -> Any | Error | ValidationError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Any | Error | ValidationError]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    endpoint_id: str,
    *,
    client: httpx.Client,
    body: RestartEndpointRequest | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Any | Error | ValidationError]:
    """Restart Endpoint

     Restart an entire endpoint or a single component within an endpoint.

    Args:
        endpoint_id (str):
        body (RestartEndpointRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | ValidationError]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    endpoint_id: str,
    *,
    client: httpx.Client,
    body: dict,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Any | Error | ValidationError]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
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
    endpoint_id: str,
    *,
    client: httpx.AsyncClient,
    body: RestartEndpointRequest | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Any | Error | ValidationError]:
    """Restart Endpoint

     Restart an entire endpoint or a single component within an endpoint.

    Args:
        endpoint_id (str):
        body (RestartEndpointRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | ValidationError]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    endpoint_id: str,
    *,
    client: httpx.AsyncClient,
    body: dict,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Any | Error | ValidationError]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        client=client,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
