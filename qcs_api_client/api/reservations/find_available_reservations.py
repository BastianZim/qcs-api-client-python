import datetime
from typing import Any

import httpx
from rfc3339 import rfc3339
from tenacity import retry

from ...models.error import Error
from ...models.find_available_reservations_response import FindAvailableReservationsResponse
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["quantumProcessorId"] = quantum_processor_id

    json_start_time_from = rfc3339(start_time_from)
    params["startTimeFrom"] = json_start_time_from

    params["duration"] = duration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/reservations:findAvailable",
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | FindAvailableReservationsResponse | None:
    if response.status_code == 200:
        response_200 = FindAvailableReservationsResponse.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Error | FindAvailableReservationsResponse]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | FindAvailableReservationsResponse]:
    """Find Available Reservations

     List currently available reservations on the requested Rigetti quantum computer.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        quantum_processor_id (str):
        start_time_from (datetime.datetime):
        duration (str): Formatted as specified for golang
            https://golang.org/pkg/time/#ParseDuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FindAvailableReservationsResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        quantum_processor_id=quantum_processor_id,
        start_time_from=start_time_from,
        duration=duration,
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
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | FindAvailableReservationsResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
        quantum_processor_id=quantum_processor_id,
        start_time_from=start_time_from,
        duration=duration,
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
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | FindAvailableReservationsResponse]:
    """Find Available Reservations

     List currently available reservations on the requested Rigetti quantum computer.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        quantum_processor_id (str):
        start_time_from (datetime.datetime):
        duration (str): Formatted as specified for golang
            https://golang.org/pkg/time/#ParseDuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FindAvailableReservationsResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        quantum_processor_id=quantum_processor_id,
        start_time_from=start_time_from,
        duration=duration,
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
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | FindAvailableReservationsResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
        quantum_processor_id=quantum_processor_id,
        start_time_from=start_time_from,
        duration=duration,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
