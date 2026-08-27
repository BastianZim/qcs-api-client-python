from typing import Any
from urllib.parse import quote

import httpx
from tenacity import retry

from ...models.billing_customer import BillingCustomer
from ...models.error import Error
from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/billingCustomer".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> BillingCustomer | Error | None:
    if response.status_code == 200:
        response_200 = BillingCustomer.from_dict(response.json())

        return response_200

    raise QCSHTTPStatusError(
        message=f"Unexpected response: status code {response.status_code}",
        response=response,
    )


def _build_response(*, response: httpx.Response) -> Response[BillingCustomer | Error]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    user_id: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[BillingCustomer | Error]:
    """Retrieve billing customer for a QCS user account.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingCustomer | Error]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        user_id=user_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    user_id: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[BillingCustomer | Error]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    user_id: str,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[BillingCustomer | Error]:
    """Retrieve billing customer for a QCS user account.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingCustomer | Error]
    """

    httpx_request_kwargs = httpx_request_kwargs or {}
    kwargs = _get_kwargs(
        user_id=user_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    user_id: str,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: dict[str, Any] | None = None,
) -> Response[BillingCustomer | Error]:
    httpx_request_kwargs = httpx_request_kwargs or {}

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
