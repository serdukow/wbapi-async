from __future__ import annotations

import httpx
import pytest

from tests.conftest import ALL_SCOPES, Recorder, make_token
from wbapi import WBApi
from wbapi.exceptions import WBAuthError, WBConfigurationError
from wbapi.utils import Scope, TokenKind


SECTIONS = (
    "general",
    "items",
    "orders_fbs",
    "orders_dbw",
    "orders_dbs",
    "in_store_pickup",
    "orders_fbw",
    "promotion",
    "communications",
    "rates",
    "analytics",
    "reports",
    "finances",
    "wbd",
)


@pytest.mark.parametrize("section", SECTIONS)
def test_every_section_is_available(api: WBApi, section: str) -> None:
    assert hasattr(api, section)


def test_token_is_decoded_on_init(api: WBApi) -> None:
    assert api.token.kind is not None
    assert api.token.seller_id == "seller-1"


@pytest.mark.parametrize("token", ["", "   ", None, 123])
def test_invalid_token_rejected(token: object) -> None:
    with pytest.raises(WBConfigurationError, match="токен"):
        WBApi(token=token)  # type: ignore[arg-type]


def test_repr_hides_token() -> None:
    api = WBApi(token=make_token(scopes=ALL_SCOPES))
    assert "eyJ" not in repr(api)


async def test_request_goes_to_the_endpoint_host(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": []})
    await api.orders_fbs.get_orders_new()
    assert recorder.last.url.host == "marketplace-api.wildberries.ru"


async def test_token_is_sent(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": []})
    await api.orders_fbs.get_orders_new()
    assert recorder.last.headers["authorization"].startswith("eyJ")


async def test_path_parameters_are_substituted(api: WBApi, recorder: Recorder) -> None:
    recorder.add(None, 204)
    await api.orders_fbs.cancel_order(order_id=13833711)
    assert recorder.last.url.path == "/api/v3/orders/13833711/cancel"


async def test_query_parameters_use_api_names(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": [], "next": 0})
    await api.orders_fbs.get_orders(limit=10, next_=77)
    assert dict(recorder.last.url.params) == {"limit": "10", "next": "77"}


async def test_empty_parameters_are_skipped(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": [], "next": 0})
    await api.orders_fbs.get_orders(limit=10, next_=0, date_from=None)
    assert "dateFrom" not in recorder.last.url.params


async def test_body_fields_use_api_names(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"stickers": []})
    await api.orders_fbs.get_supplies_trbx_stickers(supply_id="WB-GI-1", trbx_ids=["WB-TRBX-1"], type_="svg")
    assert recorder.body() == {"trbxIds": ["WB-TRBX-1"]}
    assert recorder.last.url.params["type"] == "svg"


@pytest.mark.parametrize("unsafe", ["../../admin", "a/b", "a?b", "a#b", "a b"])
async def test_unsafe_path_value_is_rejected(api: WBApi, recorder: Recorder, unsafe: str) -> None:
    """A value must not retarget the request to another endpoint."""
    with pytest.raises(ValueError, match="Недопустимое значение"):
        await api.orders_fbs.get_supplies_by_id(supply_id=unsafe)
    assert recorder.count == 0


async def test_scope_is_checked_before_request(recorder: Recorder) -> None:
    token = make_token(scopes=1 << Scope.CONTENT)
    async with WBApi(token=token, transport=httpx.MockTransport(recorder), max_retries=0) as api:
        with pytest.raises(WBAuthError, match="Категория токена"):
            await api.orders_fbs.get_orders_new()
    assert recorder.count == 0


async def test_scope_check_passes_when_allowed(recorder: Recorder) -> None:
    token = make_token(scopes=1 << Scope.MARKETPLACE)
    recorder.add({"orders": []})
    async with WBApi(token=token, transport=httpx.MockTransport(recorder), max_retries=0) as api:
        await api.orders_fbs.get_orders_new()
    assert recorder.count == 1


async def test_token_without_mask_is_not_blocked(recorder: Recorder) -> None:
    recorder.add({"orders": []})
    async with WBApi(token=make_token(), transport=httpx.MockTransport(recorder), max_retries=0) as api:
        await api.orders_fbs.get_orders_new()
    assert recorder.count == 1


async def test_sandbox_switches_the_host(recorder: Recorder) -> None:
    recorder.add({"orders": []})
    async with WBApi(
        token=make_token(acc=2, scopes=ALL_SCOPES),
        transport=httpx.MockTransport(recorder),
        max_retries=0,
        sandbox=True,
    ) as api:
        await api.orders_fbs.get_orders_new()
    assert recorder.last.url.host == "marketplace-api-sandbox.wildberries.ru"


async def test_sandbox_refuses_when_unavailable(recorder: Recorder) -> None:
    async with WBApi(
        token=make_token(acc=2, scopes=ALL_SCOPES),
        transport=httpx.MockTransport(recorder),
        max_retries=0,
        sandbox=True,
    ) as api:
        with pytest.raises(WBConfigurationError, match="sandbox"):
            await api.finances.get_account_balance()
    assert recorder.count == 0


async def test_context_manager_closes_the_pool(recorder: Recorder) -> None:
    async with WBApi(token=make_token(scopes=ALL_SCOPES), transport=httpx.MockTransport(recorder)) as api:
        assert not api._session._client.is_closed
    assert api._session._client.is_closed


async def test_empty_response_becomes_none(api: WBApi, recorder: Recorder) -> None:
    recorder.add_raw(httpx.Response(204))
    assert await api.orders_fbs.cancel_order(order_id=1) is None


async def test_sandbox_accepts_a_test_token() -> None:
    api = WBApi(token=make_token(acc=2), sandbox=True)
    assert api.sandbox
    assert api.token.kind is TokenKind.TEST


async def test_unknown_token_kind_is_not_blocked() -> None:
    api = WBApi(token="not-a-jwt", sandbox=True)
    assert api.sandbox
