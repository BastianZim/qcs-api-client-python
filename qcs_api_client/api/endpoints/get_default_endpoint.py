from typing import Any
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.endpoint import Endpoint
from ...models.error import Error
from ...models.validation_error import ValidationError
from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    quantum_processor_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/quantumProcessors/{quantum_processor_id}/endpoints:getDefault".format(
            quantum_processor_id=quote(str(quantum_processor_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Endpoint | Error | ValidationError | None:
    if response.status_code == 200:
        response_200 = Endpoint.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Endpoint | Error | ValidationError]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    quantum_processor_id: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Endpoint | Error | ValidationError]:
    r"""Get Default Endpoint

     Retrieve the endpoint set as \"default\" for the given Quantum Processor.

    If no endpoint is set as the default, return \"not found.\"

    Args:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Endpoint | Error | ValidationError]
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
) -> Response[Endpoint | Error | ValidationError]:
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
) -> Response[Endpoint | Error | ValidationError]:
    r"""Get Default Endpoint

     Retrieve the endpoint set as \"default\" for the given Quantum Processor.

    If no endpoint is set as the default, return \"not found.\"

    Args:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Endpoint | Error | ValidationError]
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
) -> Response[Endpoint | Error | ValidationError]:
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
