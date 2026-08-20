from __future__ import annotations

from typing import Any


__all__ = (
    "WBError",
    "WBAPIError",
    "WBAuthError",
    "WBForbiddenError",
    "WBNotFoundError",
    "WBValidationError",
    "WBRateLimitError",
    "WBServerError",
    "WBTransportError",
    "WBTimeoutError",
    "WBConnectionError",
    "WBConfigurationError",
    "WBDecodeError",
)

_MAX_MESSAGE_LEN = 500


class WBError(Exception):
    """Общий предок всех исключений библиотеки."""


class WBConfigurationError(WBError, ValueError):
    """Клиент вызван неправильно."""


class WBDecodeError(WBError):
    """Ответ не совпал с описанием в спецификации."""

    def __init__(self, message: str, *, path: str, payload: object) -> None:
        self.path = path
        self.payload = payload
        super().__init__(message)


class WBTransportError(WBError):
    """Запрос не дошёл до ответа."""


class WBTimeoutError(WBTransportError, TimeoutError):
    """Таймаут запроса."""


class WBConnectionError(WBTransportError, ConnectionError):
    """Соединение не установлено."""


def _as_text(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return None


def _extract_message(payload: Any) -> str | None:
    if isinstance(payload, str):
        return payload.strip() or None

    if isinstance(payload, dict):
        # RFC 7807: the short title and the longer detail read better together.
        title = payload.get("title")
        detail = payload.get("detail")
        if isinstance(title, str) and isinstance(detail, str):
            title, detail = title.strip(), detail.strip()
            if title and detail and title != detail:
                return f"{title}: {detail}"

        for key in ("errorText", "detail", "message", "title", "error", "errors"):
            value = payload.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
            if isinstance(value, list | dict) and value:
                nested = _extract_message(value)
                if nested:
                    return nested
        return None

    if isinstance(payload, list):
        for item in payload:
            nested = _extract_message(item)
            if nested:
                return nested
        return None

    return None


class WBAPIError(WBError):
    """Ошибка от API. Поля problem+json доступны как атрибуты."""

    __slots__ = ("status_code", "payload", "code", "origin", "request_id", "method", "path")

    def __init__(
        self,
        message: str | None = None,
        *,
        status_code: int = 0,
        payload: Any = None,
        request_id: str | None = None,
        method: str | None = None,
        path: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.payload = payload

        problem = payload if isinstance(payload, dict) else {}
        self.code = _as_text(problem.get("code"))
        self.origin = _as_text(problem.get("origin"))
        self.request_id = request_id or _as_text(problem.get("requestId"))
        self.method = method
        self.path = path
        super().__init__(self._build_message(message))

    def _build_message(self, message: str | None) -> str:
        text = message or _extract_message(self.payload)
        has_text = bool(text)
        if not text:
            text = f"HTTP {self.status_code}" if self.status_code else "Request failed"
        if len(text) > _MAX_MESSAGE_LEN:
            text = text[:_MAX_MESSAGE_LEN] + "…"

        context = []
        if self.status_code and has_text:
            context.append(f"HTTP {self.status_code}")
        if self.method and self.path:
            context.append(f"{self.method} {self.path}")
        elif self.path:
            context.append(self.path)
        if self.code:
            context.append(f"code={self.code}")
        if self.request_id:
            context.append(f"request_id={self.request_id}")

        return f"{text} ({', '.join(context)})" if context else text

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}({str(self)!r}, status_code={self.status_code}, "
            f"request_id={self.request_id!r})"
        )


class WBAuthError(WBAPIError):
    """401."""


class WBForbiddenError(WBAPIError):
    """403."""


class WBNotFoundError(WBAPIError):
    """404."""


class WBValidationError(WBAPIError):
    """400, 409, 422."""


class WBRateLimitError(WBAPIError):
    """429."""

    __slots__ = ("retry_after",)

    def __init__(self, *args: Any, retry_after: float | None = None, **kwargs: Any) -> None:
        self.retry_after = retry_after
        super().__init__(*args, **kwargs)


class WBServerError(WBAPIError):
    """5xx."""


_STATUS_MAP: dict[int, type[WBAPIError]] = {
    400: WBValidationError,
    401: WBAuthError,
    403: WBForbiddenError,
    404: WBNotFoundError,
    409: WBValidationError,
    422: WBValidationError,
    429: WBRateLimitError,
}


def error_for_status(status_code: int) -> type[WBAPIError]:
    mapped = _STATUS_MAP.get(status_code)
    if mapped is not None:
        return mapped
    if status_code >= 500:
        return WBServerError
    return WBAPIError
