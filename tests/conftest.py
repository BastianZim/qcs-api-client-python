from unittest.mock import AsyncMock, Mock

import pytest
from qcs_api_client_common.configuration import SecretAccessToken

from qcs_api_client.client import ClientConfiguration


@pytest.fixture
def client_configuration() -> ClientConfiguration:
    config = AsyncMock(spec=ClientConfiguration)
    config.api_url = "https://example.com/api/v1/"
    config.get_bearer_access_token = Mock(return_value=SecretAccessToken("mock_client_token"))
    config.get_bearer_access_token_async = AsyncMock(return_value=SecretAccessToken("mock_client_token"))
    return config
