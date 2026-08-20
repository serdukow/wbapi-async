"""Error mapping — including the payload shapes that used to crash the client."""

from __future__ import annotations

from typing import Any

import pytest

from wbapi.exceptions import (
    WBAPIError,
    WBAuthError,
    WBError,
    WBForbiddenError,
    WBNotFoundError,
    WBRateLimitError,
    WBServerError,
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
def test_status_maps_to_specific_exception(status: int, expected: type[WBAPIError]) -> None:
    assert error_for_status(status) is expected


@pytest.mark.parametrize(
    "payload",
    [
        [{"code": "BAD", "message": "broken"}],  # regression: list crashed **kwargs
        ["just a string in a list"],
        "plain text body",
        None,
        [],
        {"nested": {"errors": ["deep"]}},
        42,
    ],
)
def test_any_payload_shape_constructs(payload: Any) -> None:
    """A non-dict payload must never raise while building the exception."""
    error = WBAPIError(status_code=400, payload=payload)
    assert error.payload == payload
    assert str(error)
    assert isinstance(error, WBError)


def test_message_extracted_from_list_payload() -> None:
    error = WBAPIError(status_code=400, payload=[{"errorText": "bad nmID"}])
    assert "bad nmID" in str(error)


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ({"errorText": "e"}, "e"),
        ({"detail": "d"}, "d"),
        ({"message": "m"}, "m"),
        ({"title": "t"}, "t"),
        ({"errors": ["first", "second"]}, "first"),
    ],
)
def test_message_extracted_from_known_keys(payload: dict[str, Any], expected: str) -> None:
    assert expected in str(WBAPIError(status_code=400, payload=payload))


def test_message_falls_back_to_status() -> None:
    assert "404" in str(WBAPIError(status_code=404, payload=None))


def test_context_included() -> None:
    error = WBAPIError(
        status_code=400,
        payload={"errorText": "x"},
        method="POST",
        path="/content/v2/cards/update",
        request_id="req-1",
    )
    text = str(error)
    assert "POST" in text and "req-1" in text


def test_long_message_truncated() -> None:
    error = WBAPIError(status_code=400, payload={"errorText": "x" * 5000})
    assert len(str(error)) < 700


def test_rate_limit_carries_retry_after() -> None:
    error = WBRateLimitError(status_code=429, payload=None, retry_after=12.5)
    assert error.retry_after == 12.5


def test_all_errors_share_a_root() -> None:
    for cls in (WBAuthError, WBNotFoundError, WBRateLimitError, WBServerError):
        assert issubclass(cls, WBAPIError)
        assert issubclass(cls, WBError)


class TestProblemDetails:
    """Wildberries returns RFC 7807 ``application/problem+json`` bodies."""

    @staticmethod
    def _body(**overrides: Any) -> dict[str, Any]:
        body = {
            "title": "Не авторизован",
            "detail": "Токен не прошёл проверку",
            "code": "AUTH_401",
            "requestId": "d4f1-9a",
            "origin": "seller-auth",
            "status": 401,
            "statusText": "Unauthorized",
            "timestamp": "2026-08-20T10:00:00Z",
        }
        body.update(overrides)
        return body

    def test_title_and_detail_are_combined(self) -> None:
        error = WBAPIError(status_code=401, payload=self._body())
        assert "Не авторизован" in str(error)
        assert "Токен не прошёл проверку" in str(error)

    def test_internal_code_is_exposed(self) -> None:
        assert WBAPIError(status_code=401, payload=self._body()).code == "AUTH_401"

    def test_origin_service_is_exposed(self) -> None:
        assert WBAPIError(status_code=401, payload=self._body()).origin == "seller-auth"

    def test_request_id_read_from_body(self) -> None:
        assert WBAPIError(status_code=401, payload=self._body()).request_id == "d4f1-9a"

    def test_header_request_id_wins_over_body(self) -> None:
        error = WBAPIError(status_code=401, payload=self._body(), request_id="from-header")
        assert error.request_id == "from-header"

    def test_code_appears_in_message(self) -> None:
        assert "AUTH_401" in str(WBAPIError(status_code=401, payload=self._body()))

    def test_identical_title_and_detail_not_duplicated(self) -> None:
        body = self._body(title="Ошибка", detail="Ошибка")
        assert str(WBAPIError(status_code=400, payload=body)).count("Ошибка") == 1

    def test_missing_problem_fields_are_none(self) -> None:
        error = WBAPIError(status_code=500, payload={"detail": "x"})
        assert error.code is None
        assert error.origin is None

    def test_non_dict_payload_leaves_fields_none(self) -> None:
        error = WBAPIError(status_code=400, payload=[{"code": "ignored"}])
        assert error.code is None
        assert error.origin is None
