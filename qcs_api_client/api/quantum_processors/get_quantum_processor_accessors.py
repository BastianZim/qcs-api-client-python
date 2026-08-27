from typing import Any
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.list_quantum_processor_accessors_response import ListQuantumProcessorAccessorsResponse
from ...models.validation_error import ValidationError
from ...types import Response
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    quantum_processor_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/quantumProcessors/{quantum_processor_id}/accessors".format(
            quantum_processor_id=quote(str(quantum_processor_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | ListQuantumProcessorAccessorsResponse | ValidationError:
    if response.status_code == 200:
        response_200 = ListQuantumProcessorAccessorsResponse.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, response: httpx.Response
) -> Response[Error | ListQuantumProcessorAccessorsResponse | ValidationError]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    quantum_processor_id: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListQuantumProcessorAccessorsResponse | ValidationError]:
    """Get Quantum Processor Accessors

     Retrieve a single `QuantumProcessor` by ID.

    Args:
        quantum_processor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListQuantumProcessorAccessorsResponse | ValidationError]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    quantum_processor_id: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListQuantumProcessorAccessorsResponse | ValidationError]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    quantum_processor_id: str,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListQuantumProcessorAccessorsResponse | ValidationError]:
    """Get Quantum Processor Accessors

     Retrieve a single `QuantumProcessor` by ID.

    Args:
        quantum_processor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListQuantumProcessorAccessorsResponse | ValidationError]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    quantum_processor_id: str,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListQuantumProcessorAccessorsResponse | ValidationError]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
