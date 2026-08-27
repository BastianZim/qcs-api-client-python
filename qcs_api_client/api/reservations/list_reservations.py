from typing import Any

import httpx
from tenacity import retry

from ...models.account_type import AccountType
from ...models.error import Error
from ...models.list_reservations_response import ListReservationsResponse
from ...models.list_reservations_show_deleted import ListReservationsShowDeleted
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListReservationsShowDeleted | Unset = ListReservationsShowDeleted.FALSE,
    x_qcs_account_id: str | Unset = UNSET,
    x_qcs_account_type: AccountType | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_qcs_account_id, Unset):
        headers["X-QCS-ACCOUNT-ID"] = x_qcs_account_id

    if not isinstance(x_qcs_account_type, Unset):
        headers["X-QCS-ACCOUNT-TYPE"] = str(x_qcs_account_type)

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
        "url": "/v1/reservations",
        "params": params,
    }

    _kwargs["headers"] = headers
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
    *,
    client: httpx.Client,
    filter_: str | Unset = UNSET,
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListReservationsShowDeleted | Unset = ListReservationsShowDeleted.FALSE,
    x_qcs_account_id: str | Unset = UNSET,
    x_qcs_account_type: AccountType | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListReservationsResponse]:
    """List Reservations

     List existing reservations for the authenticated user,
    or a target user when specifying `X-QCS-ACCOUNT-ID` and `X-QCS-ACCOUNT-TYPE`
    headers.

    Available filter fields include:

    * `startTime` - timestamp
    * `endTime` - timestamp
    * `createdTime` - timestamp
    * `price` - integer
    * `cancelled` - boolean (deprecated, use `showDeleted` parameter)
    * `quantumProcessorId` - string

    Available order fields include:

    * `startTime` - timestamp
    * `endTime` - timestamp
    * `createdTime` - timestamp
    * `price` - integer

    Args:
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
        show_deleted (ListReservationsShowDeleted | Unset):  Default:
            ListReservationsShowDeleted.FALSE.
        x_qcs_account_id (str | Unset): userId for `accountType` "user", group name for
            `accountType` "group".
        x_qcs_account_type (AccountType | Unset): There are two types of accounts within QCS: user
            (representing a single user in Okta) and group (representing one or more users in Okta).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListReservationsResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        filter_=filter_,
        order=order,
        page_size=page_size,
        page_token=page_token,
        show_deleted=show_deleted,
        x_qcs_account_id=x_qcs_account_id,
        x_qcs_account_type=x_qcs_account_type,
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
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListReservationsShowDeleted | Unset = ListReservationsShowDeleted.FALSE,
    x_qcs_account_id: str | Unset = UNSET,
    x_qcs_account_type: AccountType | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListReservationsResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        order=order,
        page_size=page_size,
        page_token=page_token,
        show_deleted=show_deleted,
        x_qcs_account_id=x_qcs_account_id,
        x_qcs_account_type=x_qcs_account_type,
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
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListReservationsShowDeleted | Unset = ListReservationsShowDeleted.FALSE,
    x_qcs_account_id: str | Unset = UNSET,
    x_qcs_account_type: AccountType | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListReservationsResponse]:
    """List Reservations

     List existing reservations for the authenticated user,
    or a target user when specifying `X-QCS-ACCOUNT-ID` and `X-QCS-ACCOUNT-TYPE`
    headers.

    Available filter fields include:

    * `startTime` - timestamp
    * `endTime` - timestamp
    * `createdTime` - timestamp
    * `price` - integer
    * `cancelled` - boolean (deprecated, use `showDeleted` parameter)
    * `quantumProcessorId` - string

    Available order fields include:

    * `startTime` - timestamp
    * `endTime` - timestamp
    * `createdTime` - timestamp
    * `price` - integer

    Args:
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
        show_deleted (ListReservationsShowDeleted | Unset):  Default:
            ListReservationsShowDeleted.FALSE.
        x_qcs_account_id (str | Unset): userId for `accountType` "user", group name for
            `accountType` "group".
        x_qcs_account_type (AccountType | Unset): There are two types of accounts within QCS: user
            (representing a single user in Okta) and group (representing one or more users in Okta).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListReservationsResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        filter_=filter_,
        order=order,
        page_size=page_size,
        page_token=page_token,
        show_deleted=show_deleted,
        x_qcs_account_id=x_qcs_account_id,
        x_qcs_account_type=x_qcs_account_type,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    filter_: str | Unset = UNSET,
    order: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: ListReservationsShowDeleted | Unset = ListReservationsShowDeleted.FALSE,
    x_qcs_account_id: str | Unset = UNSET,
    x_qcs_account_type: AccountType | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListReservationsResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        order=order,
        page_size=page_size,
        page_token=page_token,
        show_deleted=show_deleted,
        x_qcs_account_id=x_qcs_account_id,
        x_qcs_account_type=x_qcs_account_type,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
