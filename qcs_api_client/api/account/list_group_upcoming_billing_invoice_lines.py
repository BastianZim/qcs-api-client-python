from typing import Any
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.error import Error
from ...models.list_account_billing_invoice_lines_response import ListAccountBillingInvoiceLinesResponse
from ...types import UNSET, Response, Unset
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    group_name: str,
    *,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageToken"] = page_token

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/{group_name}/billingInvoices:listUpcomingLines".format(
            group_name=quote(str(group_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Error | ListAccountBillingInvoiceLinesResponse | None:
    if response.status_code == 200:
        response_200 = ListAccountBillingInvoiceLinesResponse.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[Error | ListAccountBillingInvoiceLinesResponse]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    group_name: str,
    *,
    client: httpx.Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListAccountBillingInvoiceLinesResponse]:
    """List invoice lines for QCS group billing customer upcoming invoice.

    Args:
        group_name (str):
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAccountBillingInvoiceLinesResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
        page_token=page_token,
        page_size=page_size,
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
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListAccountBillingInvoiceLinesResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
        client=client,
        page_token=page_token,
        page_size=page_size,
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
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListAccountBillingInvoiceLinesResponse]:
    """List invoice lines for QCS group billing customer upcoming invoice.

    Args:
        group_name (str):
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAccountBillingInvoiceLinesResponse]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        group_name=group_name,
        page_token=page_token,
        page_size=page_size,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    group_name: str,
    *,
    client: httpx.AsyncClient,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[Error | ListAccountBillingInvoiceLinesResponse]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        group_name=group_name,
        client=client,
        page_token=page_token,
        page_size=page_size,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
