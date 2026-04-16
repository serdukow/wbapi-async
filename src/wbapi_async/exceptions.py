from typing import Any


class BaseWbAPIError(Exception):
    pass


class WbAPIError(BaseWbAPIError):
    def __init__(self, http_status: int = 0, **kwargs: Any) -> None:
        self.http_status = http_status
        self.detail: dict[str, Any] = kwargs
        msg = kwargs.get("errorText") or kwargs.get("detail") or kwargs.get("title") or str(kwargs)
        super().__init__(msg)


class TokenValidationError(BaseWbAPIError):
    pass


class PaginationNotSupported(BaseWbAPIError):
    pass
