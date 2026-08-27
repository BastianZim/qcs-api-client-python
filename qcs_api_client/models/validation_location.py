from enum import Enum


class ValidationLocation(str, Enum):
    BODY = "body"
    HEADER = "header"
    PATH = "path"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
