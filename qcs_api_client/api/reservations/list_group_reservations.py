from typing import Any
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.list_group_reservations_show_deleted import ListGroupReservationsShowDeleted
from ...models.list_reservations_response import ListReservationsResponse
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    group_name: str,
    *,
    filter_: str | Unset = UNSET,
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListGroupReservationsShowDeleted | Unset = ListGroupReservationsShowDeleted.FALSE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["order"] = order

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    json_show_deleted: str | Unset = UNSET
    if not isinstance(show_deleted, Unset):
        json_show_deleted = show_deleted.value

    params["showDeleted"] = json_show_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/{group_name}/reservations".format(
            group_name=quote(str(group_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | ListReservationsResponse | None:
    if response.status_code == 200:
        response_200 = ListReservationsResponse.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Error | ListReservationsResponse]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    group_name: str,
    *,
    client: httpx.Client,
    filter_: str | Unset = UNSET,
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListGroupReservationsShowDeleted | Unset = ListGroupReservationsShowDeleted.FALSE,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListReservationsResponse]:
    """List Group Reservations

     List existing reservations for the requested group.

    Available filter fields include:

    * `startTime` - timestamp
    * `endTime` - timestamp
    * `createdTime` - timestamp
    * `price` - integer
    * `quantumProcessorId` - string

    Available order fields include:

    * `startTime` - timestamp
    * `endTime` - timestamp
    * `createdTime` - timestamp
    * `price` - integer

    Args:
        group_name (str):
        filter_ (str | Unset): A string conforming to a *limited* set of the filtering operations
            described in [Google AIP 160](https://google.aip.dev/160).

            * Expressions are always of the form `{field} {operator} {value}` and may be grouped with
            `()` and joined with `AND` or `OR`.
            * Fields are specific to the route in question, but are typically a subset of attributes
            of the requested resource.
            * Operators are limited to `=`, `>`, `>=`, `<`, `<=`, and `!=`.
            * Values may take the following forms:
              * `true` or `false` for boolean fields
              * a number
              * a string (include surrounding `"`s),
              * a duration string (include surrounding `"`s). Valid time units are "ns", "us" (or
            "µs"), "ms", "s", "m", "h".
              * a date string (include surrounding `"`s). Should be formatted [RFC3339
            5.6](https://tools.ietf.org/html/rfc3339#section-5.6).

            For example, `startTime >= "2020-06-24T22:00:00.000Z" OR (duration >= "15m" AND endTime <
            "2020-06-24T22:00:00.000Z")`.
        order (str | Unset): A string conforming to order specification described in [Google
            AIP 132](https://google.aip.dev/132#ordering).

            * Fields are specific to the route in question, but are typically a subset
            of attributes of the requested resource.
            * May include a comma separated list of many fields.
            * Fields are sorted in *ascending* order unless the field is followed by `DESC`.

            For example, `quantumProcessorId, startTime DESC`.
        page_size (int | Unset):
        page_token (str | Unset):
        show_deleted (ListGroupReservationsShowDeleted | Unset):  Default:
            ListGroupReservationsShowDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListReservationsResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
        filter_=filter_,
        order=order,
        page_size=page_size,
        page_token=page_token,
        show_deleted=show_deleted,
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
    filter_: str | Unset = UNSET,
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListGroupReservationsShowDeleted | Unset = ListGroupReservationsShowDeleted.FALSE,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListReservationsResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
        client=client,
        filter_=filter_,
        order=order,
        page_size=page_size,
        page_token=page_token,
        show_deleted=show_deleted,
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
    filter_: str | Unset = UNSET,
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListGroupReservationsShowDeleted | Unset = ListGroupReservationsShowDeleted.FALSE,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListReservationsResponse]:
    """List Group Reservations

     List existing reservations for the requested group.

    Available filter fields include:

    * `startTime` - timestamp
    * `endTime` - timestamp
    * `createdTime` - timestamp
    * `price` - integer
    * `quantumProcessorId` - string

    Available order fields include:

    * `startTime` - timestamp
    * `endTime` - timestamp
    * `createdTime` - timestamp
    * `price` - integer

    Args:
        group_name (str):
        filter_ (str | Unset): A string conforming to a *limited* set of the filtering operations
            described in [Google AIP 160](https://google.aip.dev/160).

            * Expressions are always of the form `{field} {operator} {value}` and may be grouped with
            `()` and joined with `AND` or `OR`.
            * Fields are specific to the route in question, but are typically a subset of attributes
            of the requested resource.
            * Operators are limited to `=`, `>`, `>=`, `<`, `<=`, and `!=`.
            * Values may take the following forms:
              * `true` or `false` for boolean fields
              * a number
              * a string (include surrounding `"`s),
              * a duration string (include surrounding `"`s). Valid time units are "ns", "us" (or
            "µs"), "ms", "s", "m", "h".
              * a date string (include surrounding `"`s). Should be formatted [RFC3339
            5.6](https://tools.ietf.org/html/rfc3339#section-5.6).

            For example, `startTime >= "2020-06-24T22:00:00.000Z" OR (duration >= "15m" AND endTime <
            "2020-06-24T22:00:00.000Z")`.
        order (str | Unset): A string conforming to order specification described in [Google
            AIP 132](https://google.aip.dev/132#ordering).

            * Fields are specific to the route in question, but are typically a subset
            of attributes of the requested resource.
            * May include a comma separated list of many fields.
            * Fields are sorted in *ascending* order unless the field is followed by `DESC`.

            For example, `quantumProcessorId, startTime DESC`.
        page_size (int | Unset):
        page_token (str | Unset):
        show_deleted (ListGroupReservationsShowDeleted | Unset):  Default:
            ListGroupReservationsShowDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListReservationsResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        group_name=group_name,
        filter_=filter_,
        order=order,
        page_size=page_size,
        page_token=page_token,
        show_deleted=show_deleted,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    group_name: str,
    *,
    client: httpx.AsyncClient,
    filter_: str | Unset = UNSET,
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListGroupReservationsShowDeleted | Unset = ListGroupReservationsShowDeleted.FALSE,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListReservationsResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
        client=client,
        filter_=filter_,
        order=order,
        page_size=page_size,
        page_token=page_token,
        show_deleted=show_deleted,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
