from __future__ import annotations

from typing import Any

import pytest

from wbapi.exceptions import (
    WBAPIError,
    WBAuthError,
    WBConfigurationError,
    WBConnectionError,
    WBDecodeError,
    WBError,
    WBForbiddenError,
    WBNotFoundError,
    WBRateLimitError,
    WBServerError,
    WBTimeoutError,
    WBTransportError,
    WBValidationError,
    error_for_status,
)


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        (400, WBValidationError),
        (401, WBAuthError),
        (403, WBForbiddenError),
        (404, WBNotFoundError),
        (409, WBValidationError),
        (422, WBValidationError),
        (429, WBRateLimitError),
        (500, WBServerError),
        (503, WBServerError),
        (418, WBAPIError),
    ],
)
def test_status_maps_to_a_specific_class(status: int, expected: type) -> None:
    assert error_for_status(status) is expected


@pytest.mark.parametrize(
    "payload",
    [
        [{"code": "BAD", "message": "сломалось"}],
        ["строка в списке"],
        "просто текст",
        None,
        [],
        {"nested": {"errors": ["глубоко"]}},
        42,
    ],
)
def test_any_payload_shape_is_accepted(payload: Any) -> None:
    """An error body is not always an object; that must not crash the client."""
    error = WBAPIError(status_code=400, payload=payload)
    assert error.payload == payload
    assert str(error)


def test_problem_details_fields_are_lifted() -> None:
    body = {
        "title": "Не авторизован",
        "detail": "Токен не прошёл проверку",
        "code": "AUTH_401",
        "requestId": "req-1",
        "origin": "seller-auth",
    }
    error = WBAPIError(status_code=401, payload=body)
    assert error.code == "AUTH_401"
    assert error.origin == "seller-auth"
    assert error.request_id == "req-1"
    assert "Не авторизован" in str(error)
    assert "Токен не прошёл проверку" in str(error)


def test_header_request_id_wins() -> None:
    error = WBAPIError(status_code=401, payload={"requestId": "из-тела"}, request_id="из-заголовка")
    assert error.request_id == "из-заголовка"


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ({"errorText": "текст"}, "текст"),
        ({"detail": "детали"}, "детали"),
        ({"message": "сообщение"}, "сообщение"),
        ({"errors": ["первая", "вторая"]}, "первая"),
        ([{"errorText": "в списке"}], "в списке"),
    ],
)
def test_message_is_extracted(payload: Any, expected: str) -> None:
    assert expected in str(WBAPIError(status_code=400, payload=payload))


def test_message_falls_back_to_status() -> None:
    assert "404" in str(WBAPIError(status_code=404, payload=None))


def test_long_message_is_trimmed() -> None:
    assert len(str(WBAPIError(status_code=400, payload={"errorText": "х" * 5000}))) < 700


def test_rate_limit_keeps_retry_after() -> None:
    assert WBRateLimitError(status_code=429, retry_after=12.5).retry_after == 12.5


def test_decode_error_keeps_context() -> None:
    error = WBDecodeError("не совпало", path="/api/v3/orders", payload={"a": 1})
    assert error.path == "/api/v3/orders"
    assert error.payload == {"a": 1}
    assert isinstance(error, WBError)


@pytest.mark.parametrize(
    "cls",
    [WBAuthError, WBForbiddenError, WBNotFoundError, WBRateLimitError, WBServerError],
)
def test_http_errors_share_a_base(cls: type) -> None:
    assert issubclass(cls, WBAPIError)
    assert issubclass(cls, WBError)


@pytest.mark.parametrize("cls", [WBTimeoutError, WBConnectionError])
def test_transport_errors_share_a_base(cls: type) -> None:
    assert issubclass(cls, WBTransportError)
    assert issubclass(cls, WBError)


def test_configuration_error_is_a_value_error() -> None:
    assert issubclass(WBConfigurationError, ValueError)
