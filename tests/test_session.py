from __future__ import annotations

import asyncio

import httpx
import pytest

from tests.conftest import ALL_SCOPES, Recorder, make_token
from wbapi import WBApi
from wbapi.exceptions import (
    WBAPIError,
    WBConnectionError,
    WBDecodeError,
    WBRateLimitError,
    WBServerError,
    WBTimeoutError,
)


async def test_success_is_not_retried(retrying_api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": []})
    await retrying_api.orders_fbs.get_orders_new()
    assert recorder.count == 1


@pytest.mark.parametrize("status", [429, 500, 502, 503, 504])
async def test_transient_status_is_retried(retrying_api: WBApi, recorder: Recorder, status: int) -> None:
    recorder.add({"errorText": "позже"}, status)
    recorder.add({"orders": []})
    await retrying_api.orders_fbs.get_orders_new()
    assert recorder.count == 2


@pytest.mark.parametrize("status", [400, 401, 403, 404, 422])
async def test_client_errors_are_not_retried(retrying_api: WBApi, recorder: Recorder, status: int) -> None:
    recorder.add({"errorText": "нет"}, status)
    with pytest.raises(WBAPIError):
        await retrying_api.orders_fbs.get_orders_new()
    assert recorder.count == 1


async def test_retries_are_bounded(retrying_api: WBApi, recorder: Recorder) -> None:
    """An endless 429 must not loop forever."""
    recorder.handle(lambda request: httpx.Response(429, json={"errorText": "лимит"}))
    with pytest.raises(WBRateLimitError):
        await retrying_api.orders_fbs.get_orders_new()
    assert recorder.count == 4


async def test_retry_after_is_capped(recorder: Recorder) -> None:
    """A huge Retry-After must not put the client to sleep for hours."""
    recorder.handle(
        lambda request: httpx.Response(429, json={"e": 1}, headers={"X-Ratelimit-Retry": "86400"})
    )
    api = WBApi(
        token=make_token(scopes=ALL_SCOPES),
        transport=httpx.MockTransport(recorder),
        max_retries=1,
        retry_backoff=0.001,
        max_retry_wait=0.05,
    )
    async with api:
        with pytest.raises(WBRateLimitError) as info:
            await asyncio.wait_for(api.orders_fbs.get_orders_new(), timeout=5)
    assert info.value.retry_after == 0.05


@pytest.mark.parametrize(
    ("raised", "expected"),
    [
        (httpx.ConnectTimeout("t"), WBTimeoutError),
        (httpx.ReadTimeout("t"), WBTimeoutError),
        (httpx.ConnectError("c"), WBConnectionError),
    ],
)
async def test_transport_failures_are_typed(
    recorder: Recorder, raised: Exception, expected: type[Exception]
) -> None:
    def explode(request: httpx.Request) -> httpx.Response:
        raise raised

    recorder.handle(explode)
    api = WBApi(
        token=make_token(scopes=ALL_SCOPES),
        transport=httpx.MockTransport(recorder),
        max_retries=1,
        retry_backoff=0.001,
    )
    async with api:
        with pytest.raises(expected):
            await api.orders_fbs.get_orders_new()
    assert recorder.count == 2


async def test_request_id_is_kept(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"errorText": "x"}, 500, **{"X-Request-Id": "req-42"})
    with pytest.raises(WBServerError) as info:
        await api.orders_fbs.get_orders_new()
    assert info.value.request_id == "req-42"


async def test_non_json_error_body_is_kept(api: WBApi, recorder: Recorder) -> None:
    recorder.add_raw(httpx.Response(502, text="<html>gateway</html>"))
    with pytest.raises(WBServerError) as info:
        await api.orders_fbs.get_orders_new()
    assert "gateway" in str(info.value.payload)


async def test_user_agent_names_the_library(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": []})
    await api.orders_fbs.get_orders_new()
    assert recorder.last.headers["user-agent"].startswith("wbapi/")


async def test_a_spec_fix_reaches_the_model(api: WBApi, recorder: Recorder) -> None:
    """Tags answer with an array where the spec describes an object."""
    recorder.add({"data": [{"id": 1, "color": "красный", "name": "Хит"}], "error": False})
    result = await api.items.get_tags()
    assert result.data[0].name == "Хит"


async def test_incompatible_response_raises_decode_error(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": [{"id": {"вложенный": "объект"}}]})
    with pytest.raises(WBDecodeError) as info:
        await api.orders_fbs.get_orders_new()
    assert info.value.path == "/api/v3/orders/new"
    assert info.value.payload is not None


def test_limiters_do_not_outlive_the_loop() -> None:
    import subprocess
    import sys
    import textwrap

    script = textwrap.dedent(
        """
        import asyncio, warnings, httpx, sys
        sys.path.insert(0, "src")
        warnings.simplefilter("error", RuntimeWarning)
        from wbapi import WBApi

        def handler(request):
            return httpx.Response(200, json={"orders": []})

        async def run():
            async with WBApi(token="t", transport=httpx.MockTransport(handler)) as api:
                await api.orders_fbs.get_orders_new()

        asyncio.run(run())
        asyncio.run(run())
        print("clean")
        """
    )
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, timeout=60)
    assert result.returncode == 0, result.stderr
    assert "clean" in result.stdout


async def test_unparsable_retry_after_is_ignored(recorder: Recorder) -> None:
    """A non-numeric Retry-After must not crash the backoff calculation."""
    recorder.add_raw(httpx.Response(429, headers={"X-Ratelimit-Retry": "soon"}))
    recorder.add({"orders": []})
    async with WBApi(
        token=make_token(scopes=ALL_SCOPES),
        transport=httpx.MockTransport(recorder),
        retry_backoff=0,
    ) as api:
        await api.orders_fbs.get_orders_new()
    assert recorder.count == 2


async def test_a_success_with_broken_json_is_typed(recorder: Recorder) -> None:
    """A 200 whose body is not JSON must raise, not leak the ValueError."""
    recorder.add_raw(httpx.Response(200, text="not json at all"))
    async with WBApi(
        token=make_token(scopes=ALL_SCOPES),
        transport=httpx.MockTransport(recorder),
        max_retries=0,
    ) as api:
        with pytest.raises(WBAPIError, match="Failed to decode"):
            await api.orders_fbs.get_orders_new()


async def test_session_repr_masks_the_token() -> None:
    api = WBApi(token=make_token(scopes=ALL_SCOPES))
    assert "***" in repr(api._session)


async def test_endpoints_sharing_a_quota_get_separate_limiters() -> None:
    from wbapi.client.session import _limiter_for

    orders = _limiter_for("/api/v3/orders", (200, 20))
    supplies = _limiter_for("/api/v3/supplies", (200, 20))

    assert orders is not supplies
    assert orders is _limiter_for("/api/v3/orders", (200, 20))


async def test_a_file_download_comes_back_as_bytes(recorder: Recorder) -> None:
    archive = b"PK\x03\x04 not json"
    recorder.add_raw(httpx.Response(200, content=archive, headers={"Content-Type": "application/zip"}))
    async with WBApi(token=make_token(scopes=ALL_SCOPES), transport=httpx.MockTransport(recorder)) as api:
        result = await api.analytics.get_nm_report_downloads_file(download_id="x")

    assert result == archive


async def test_a_number_in_a_string_field_does_not_fail_the_call(recorder: Recorder) -> None:
    """The finance report answers with sellerPromo as a number, not a string.

    msgspec turns "42" into 42 on its own but never the other way, so this
    drift used to abort the whole extraction.
    """
    recorder.add([{"rrd_id": 1, "sellerPromo": 0}, {"rrd_id": 2, "sellerPromo": 5}])
    async with WBApi(token=make_token(scopes=ALL_SCOPES), transport=httpx.MockTransport(recorder)) as api:
        rows = await api.finances.get_sales_reports_detailed(date_from="2026-01-01", date_to="2026-01-02")

    assert [row.seller_promo for row in rows] == ["0", "5"]


async def test_drift_it_cannot_reshape_still_raises(recorder: Recorder) -> None:
    """Reshaping must not paper over a response that is genuinely wrong."""
    recorder.add({"orders": [{"id": {"вложенный": "объект"}}]})
    async with WBApi(token=make_token(scopes=ALL_SCOPES), transport=httpx.MockTransport(recorder)) as api:
        with pytest.raises(WBDecodeError):
            await api.orders_fbs.get_orders_new()
