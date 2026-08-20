"""Verb dispatch, path templating, auth handling and lifecycle."""

from __future__ import annotations

import asyncio

import httpx
import pytest

from tests.mocked_api import TOKEN, MockedAPI
from wbapi import WBApi
from wbapi.exceptions import WBConfigurationError


async def test_get_sends_query_params(api: MockedAPI) -> None:
    api.add_response({"orders": []})
    await api.get("/api/v3/orders/new", params={"limit": 10, "next": 0})
    assert dict(api.get_last_request().url.params) == {"limit": "10", "next": "0"}


async def test_get_returns_wrapped_response(api: MockedAPI) -> None:
    api.add_response({"orders": [{"id": 7}]})
    response = await api.get("/api/v3/orders/new")
    assert response.orders[0].id == 7


async def test_post_sends_json_body(api: MockedAPI) -> None:
    api.add_response({"ok": True})
    await api.post("/adv/v0/rename", body={"advertId": 1, "name": "x"})
    request = api.get_last_request()
    assert request.method == "POST"
    assert b'"advertId"' in request.content


@pytest.mark.parametrize("verb", ["put", "patch", "delete"])
async def test_other_verbs_dispatch(api: MockedAPI, verb: str) -> None:
    api.add_response({"ok": True})
    await getattr(api, verb)("/api/v3/warehouses")
    assert api.get_last_request().method == verb.upper()


async def test_interpolated_path_is_sent_verbatim(api: MockedAPI) -> None:
    api.add_response({"ok": True})
    await api.patch("/api/v3/orders/13833711/cancel")
    assert api.get_last_request().url.path == "/api/v3/orders/13833711/cancel"


async def test_interpolated_path_keeps_its_own_rate_limit() -> None:
    """A concrete id must resolve back to its template, not its parent."""
    from wbapi.endpoints import rate_limit_for

    assert rate_limit_for("/api/v3/orders/13833711/cancel") == rate_limit_for(
        "/api/v3/orders/{orderId}/cancel"
    )


async def test_interpolated_path_resolves_host(api: MockedAPI) -> None:
    api.add_response({"ok": True})
    await api.get("/api/v3/supplies/WB-GI-123/orders")
    assert api.get_last_request().url.host == "marketplace-api.wildberries.ru"


async def test_params_are_query_only(api: MockedAPI) -> None:
    api.add_response({"ok": True})
    await api.get("/api/v3/supplies/WB-1", params={"limit": 5})
    request = api.get_last_request()
    assert request.url.path == "/api/v3/supplies/WB-1"
    assert dict(request.url.params) == {"limit": "5"}


async def test_token_sent_on_private_hosts(api: MockedAPI) -> None:
    api.add_response({"ok": True})
    await api.get("/api/v3/warehouses")
    assert api.get_last_request().headers["authorization"] == TOKEN


async def test_token_withheld_from_public_hosts(api: MockedAPI) -> None:
    api.add_response({"ok": True})
    await api.get("https://card.wb.ru/cards/detail")
    assert not api.get_last_request().headers.get("authorization")


async def test_concurrent_public_and_private_do_not_race(api: MockedAPI) -> None:
    """Regression: shared header state leaked or dropped tokens under gather."""
    api.set_handler(lambda request: httpx.Response(200, json={"ok": True}))

    await asyncio.gather(
        *(
            api.get("https://card.wb.ru/cards/detail") if index % 2 == 0 else api.get("/api/v3/warehouses")
            for index in range(40)
        )
    )

    for request in api.requests:
        auth = request.headers.get("authorization", "")
        if request.url.host == "card.wb.ru":
            assert not auth, "token leaked to a public host"
        else:
            assert auth == TOKEN, "private request lost its token"


async def test_user_agent_identifies_library(api: MockedAPI) -> None:
    api.add_response({"ok": True})
    await api.get("/api/v3/warehouses")
    assert api.get_last_request().headers["user-agent"].startswith("wbapi/")


async def test_custom_user_agent() -> None:
    api = MockedAPI(user_agent="app/2")
    api.add_response({})
    await api.get("/api/v3/warehouses")
    assert api.get_last_request().headers["user-agent"] == "app/2"


@pytest.mark.parametrize("token", ["", "   ", None, 123])
def test_invalid_token_rejected(token: object) -> None:
    with pytest.raises(WBConfigurationError, match="token"):
        WBApi(token=token)  # type: ignore[arg-type]


def test_repr_masks_token() -> None:
    api = WBApi(token="super-secret-value")
    assert "super-secret" not in repr(api)
    assert "alue" in repr(api)


async def test_context_manager_closes_pool() -> None:
    async with MockedAPI() as api:
        assert not api.is_closed
    assert api.is_closed


async def test_empty_body_returns_none(api: MockedAPI) -> None:
    api.add_raw_response(httpx.Response(204))
    assert await api.delete("/content/v2/tag/{id}", params={"id": 1}) is None
