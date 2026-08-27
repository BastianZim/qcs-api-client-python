from http import HTTPStatus
from json import JSONDecodeError
from typing import Any, cast

from httpx import HTTPStatusError, Response

from ..models.error import Error


class QCSHTTPStatusError(HTTPStatusError):
    def __init__(self, message: str, *, response: Response, error: Error | None = None) -> None:
        super().__init__(message, request=response.request, response=response)
        self.error = error


def raise_for_status(res: Response):
    """
    Raise the `QCSHTTPStatusError` if one occurred.
    """
    if res.request is None:
        raise RuntimeError("Cannot call `raise_for_status` as the request instance has not been set on this response.")
    elif res.status_code < HTTPStatus.BAD_REQUEST:
        return None

    message = f"QCS API call {res.request.method} {res.request.url} failed with status {res.status_code}: {res.text}"
    error = None
    try:
        error = Error.from_dict(cast(dict[str, Any], res.json()))
    except (JSONDecodeError, KeyError):
        pass

    raise QCSHTTPStatusError(message, response=res, error=error)
