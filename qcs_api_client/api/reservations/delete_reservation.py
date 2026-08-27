from typing import Any
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.reservation import Reservation
from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    reservation_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/reservations/{reservation_id}".format(
            reservation_id=quote(str(reservation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | Reservation | None:
    if response.status_code == 200:
        response_200 = Reservation.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Error | Reservation]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    reservation_id: int,
    *,
    client: httpx.Client,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | Reservation]:
    """Delete Reservation

     Cancel an existing reservation for the user.

    Args:
        reservation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Reservation]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    reservation_id: int,
    *,
    client: httpx.Client,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | Reservation]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    reservation_id: int,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | Reservation]:
    """Delete Reservation

     Cancel an existing reservation for the user.

    Args:
        reservation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Reservation]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        reservation_id=reservation_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    reservation_id: int,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | Reservation]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
