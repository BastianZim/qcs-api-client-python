from enum import Enum


class Code(str, Enum):
    ACCESS_FORBIDDEN = "access_forbidden"
    CONFLICTING_RESOURCE_ACCESS = "conflicting_resource_access"
    INTERNAL_ERROR = "internal_error"
    INVALID_REQUEST = "invalid_request"
    INVALID_TOKEN = "invalid_token"
    RESOURCE_EXISTS = "resource_exists"
    RESOURCE_NOT_FOUND = "resource_not_found"
    UNAUTHENTICATED = "unauthenticated"
    UNDER_LOAD = "under_load"
    UNIMPLEMENTED = "unimplemented"

    def __str__(self) -> str:
        return str(self.value)
