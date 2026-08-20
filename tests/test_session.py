"""Retry policy, rate limiting and response decoding."""

from __future__ import annotations

import asyncio

import httpx
import pytest

from tests.mocked_api import MockedAPI
from wbapi.exceptions import (
    WBAPIError,
    WBConnectionError,
    WBRateLimitError,
    WBServerError,
    WBTimeoutError,
)


async def test_success_is_not_retried(retrying_api: MockedAPI) -> None:
    retrying_api.add_response({"ok": True})
    await retrying_api.get("/api/v3/warehouses")
    assert retrying_api.request_count == 1


@pytest.mark.parametrize("status", [500, 502, 503, 504, 429])
async def test_transient_status_is_retried(retrying_api: MockedAPI, status: int) -> None:
    retrying_api.add_response({"e": 1}, status)
    retrying_api.add_response({"ok": True})
    await retrying_api.get("/api/v3/warehouses")
    assert retrying_api.request_count == 2


@pytest.mark.parametrize("status", [400, 401, 403, 404, 422])
async def test_client_errors_are_not_retried(retrying_api: MockedAPI, status: int) -> None:
    retrying_api.add_response({"errorText": "no"}, status)
    with pytest.raises(WBAPIError):
        await retrying_api.get("/api/v3/warehouses")
    assert retrying_api.request_count == 1


async def test_retries_are_bounded(retrying_api: MockedAPI) -> None:
    """Regression: 429 handling used to recurse without a limit."""
    retrying_api.set_handler(lambda request: httpx.Response(429, json={"errorText": "slow"}))
    with pytest.raises(WBRateLimitError):
        await retrying_api.get("/api/v3/warehouses")
    assert retrying_api.request_count == 4  # initial attempt + 3 retries


async def test_retry_after_header_is_capped() -> None:
    """A hostile Retry-After must not put the client to sleep for days."""
    api = MockedAPI(max_retries=1, max_retry_wait=0.05)
    api.set_handler(
        lambda request: httpx.Response(429, json={"e": 1}, headers={"X-Ratelimit-Retry": "86400"})
    )
    with pytest.raises(WBRateLimitError) as info:
        await asyncio.wait_for(api.get("/api/v3/warehouses"), timeout=5)
    assert info.value.retry_after == 0.05


@pytest.mark.parametrize(
    ("raised", "expected"),
    [
        (httpx.ConnectTimeout("t"), WBTimeoutError),
        (httpx.ReadTimeout("t"), WBTimeoutError),
        (httpx.ConnectError("c"), WBConnectionError),
    ],
)
async def test_transport_failures_map_to_typed_errors(raised: Exception, expected: type[Exception]) -> None:
    api = MockedAPI(max_retries=1)

    def explode(request: httpx.Request) -> httpx.Response:
        raise raised

    api.set_handler(explode)
    with pytest.raises(expected):
        await api.get("/api/v3/warehouses")
    assert api.request_count == 2


async def test_error_carries_request_id(api: MockedAPI) -> None:
    api.add_response({"errorText": "x"}, 500, **{"X-Request-Id": "abc-1"})
    with pytest.raises(WBServerError) as info:
        await api.get("/api/v3/warehouses")
    assert info.value.request_id == "abc-1"


async def test_non_json_error_body_is_preserved(api: MockedAPI) -> None:
    api.add_raw_response(httpx.Response(502, text="<html>gateway</html>"))
    with pytest.raises(WBServerError) as info:
        await api.get("/api/v3/warehouses")
    assert "gateway" in str(info.value.payload)


async def test_non_json_success_body_raises(api: MockedAPI) -> None:
    api.add_raw_response(httpx.Response(200, text="not json at all"))
    with pytest.raises(WBAPIError, match="decode"):
        await api.get("/api/v3/warehouses")


def test_limiter_is_not_shared_across_event_loops() -> None:
    """Regression: a process-wide limiter warned and misbehaved on a second loop.

    Runs in a subprocess because the check needs two top-level event loops,
    which cannot be created from inside the pytest-asyncio session.
    """
    import subprocess
    import sys
    import textwrap

    script = textwrap.dedent(
        """
        import asyncio, warnings, httpx
        warnings.simplefilter("error", RuntimeWarning)
        from wbapi import WBApi

        def handler(request):
            return httpx.Response(200, json={"ok": True})

        async def run():
            async with WBApi(token="t", transport=httpx.MockTransport(handler)) as api:
                await api.get("/api/v3/warehouses")

        asyncio.run(run())
        asyncio.run(run())
        print("clean")
        """
    )
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, timeout=60)
    assert result.returncode == 0, result.stderr
    assert "clean" in result.stdout
