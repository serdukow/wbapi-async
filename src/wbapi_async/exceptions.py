from typing import Any

from .types import Error


class BaseWbAPIError(Exception):
    pass


class WbAPIError(BaseWbAPIError):
    def __init__(self, http_status: int = 0, **kwargs: Any) -> None:
        self.error = Error(**kwargs)
        self.http_status = http_status
        super().__init__(str(self.error))


class TokenValidationError(BaseWbAPIError):
    pass
