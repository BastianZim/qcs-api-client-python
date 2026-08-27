from typing import Any

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.list_instruction_set_architecture_response import ListInstructionSetArchitectureResponse
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    *,
    page_size: int | Unset = 5,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/instructionSetArchitectures",
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | ListInstructionSetArchitectureResponse | ValidationError:
    if response.status_code == 200:
        response_200 = ListInstructionSetArchitectureResponse.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, response: httpx.Response
) -> Response[Error | ListInstructionSetArchitectureResponse | ValidationError]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    page_size: int | Unset = 5,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListInstructionSetArchitectureResponse | ValidationError]:
    """List Instruction Set Architectures

    Args:
        page_size (int | Unset):  Default: 5.
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListInstructionSetArchitectureResponse | ValidationError]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
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
    page_size: int | Unset = 5,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListInstructionSetArchitectureResponse | ValidationError]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
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
    *,
    client: httpx.AsyncClient,
    page_size: int | Unset = 5,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListInstructionSetArchitectureResponse | ValidationError]:
    """List Instruction Set Architectures

    Args:
        page_size (int | Unset):  Default: 5.
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListInstructionSetArchitectureResponse | ValidationError]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
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
    page_size: int | Unset = 5,
    page_token: str | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListInstructionSetArchitectureResponse | ValidationError]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
