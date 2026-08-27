from contextlib import asynccontextmanager, contextmanager

import httpx
from qcs_api_client_common.configuration import ClientConfiguration

from .auth import QCSAuth


def _build_client_kwargs(
    *, configuration: ClientConfiguration | None = None, kwarg_overrides: dict | None = None
) -> dict:
    """
    Return kwargs used for construction of an httpx.BaseClient.
    """
    configuration = configuration or ClientConfiguration.load_default()
    auth = QCSAuth(client_configuration=configuration)
    kwargs = dict(auth=auth, base_url=str(configuration.api_url))

    if kwarg_overrides is not None:
        kwargs.update(kwarg_overrides)

    return kwargs


@contextmanager
def build_sync_client(
    *, configuration: ClientConfiguration | None = None, client_kwargs: dict | None = None
) -> httpx.Client:
    """
    Yield a client object suitable for use with the qcs_api_client.sync API functions.
    """
    with httpx.Client(**_build_client_kwargs(configuration=configuration, kwarg_overrides=client_kwargs)) as client:
        yield client


@asynccontextmanager
async def build_async_client(
    *,
    configuration: ClientConfiguration | None = None,
    client_kwargs: dict | None = None,
) -> httpx.AsyncClient:
    """
    Yield a client object suitable for use with the qcs_api_client.asyncio API functions.
    """
    async with httpx.AsyncClient(
        **_build_client_kwargs(configuration=configuration, kwarg_overrides=client_kwargs)
    ) as client:
        yield client
