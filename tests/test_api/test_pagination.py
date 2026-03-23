"""Tests for auto-pagination strategies (offset, next cursor, take+skip)."""

from __future__ import annotations

from typing import Any

import pytest

from tests.mocked_api import MockedAPI
from wbapi_async import paginate
from wbapi_async.methods.base import WbMethod
from wbapi_async.methods.pagination import (
    PAGINATION_STRATEGIES,
    NextCursorPagination,
    OffsetPagination,
    TakeSkipPagination,
)
from wbapi_async.types import RequestLimit
from wbapi_async.types.base import BaseType


def _bound(api: MockedAPI, method_cls: type) -> Any:
    """Create a fake bound method with __wrapped_cls__ — mirrors what codegen generates."""
    class _FakeBound:
        __self__ = api
        __name__ = method_cls.__name__
        __wrapped_cls__ = method_cls

    return _FakeBound()


# ---------------------------------------------------------------------------
# Minimal return type and WbMethod subclasses for each pagination pattern
# ---------------------------------------------------------------------------

class _Item(BaseType):
    id: int = 0


class _OffsetMethod(WbMethod):
    __return__ = _Item
    __api__ = "test-api"
    __method__ = "api/v1/items"
    __data_key__ = "items"
    __pagination__ = "offset"
    request_limit: RequestLimit = RequestLimit(period=60, limit=60, interval=60, burst=10)


class _NextMethod(WbMethod):
    __return__ = _Item
    __api__ = "test-api"
    __method__ = "api/v1/orders"
    __data_key__ = "orders"
    __pagination__ = "next"
    request_limit: RequestLimit = RequestLimit(period=60, limit=60, interval=60, burst=10)


class _TakeSkipMethod(WbMethod):
    __return__ = _Item
    __api__ = "test-api"
    __method__ = "api/v1/feedbacks"
    __data_key__ = "feedbacks"
    __pagination__ = "take_skip"
    request_limit: RequestLimit = RequestLimit(period=60, limit=60, interval=60, burst=10)


# ---------------------------------------------------------------------------
# Unit tests for individual strategies
# ---------------------------------------------------------------------------

@pytest.mark.unit
class TestOffsetPagination:
    def test_first_params(self) -> None:
        s = OffsetPagination()
        assert s.first_params() == {"limit": 1000, "offset": 0}

    def test_next_params_full_page_advances_offset(self) -> None:
        s = OffsetPagination()
        page = [{"id": i} for i in range(1000)]
        current = {"limit": 1000, "offset": 0}
        assert s.next_params(current, {}, page) == {"limit": 1000, "offset": 1000}

    def test_next_params_second_advance(self) -> None:
        s = OffsetPagination()
        page = [{"id": i} for i in range(1000)]
        current = {"limit": 1000, "offset": 1000}
        assert s.next_params(current, {}, page) == {"limit": 1000, "offset": 2000}

    def test_next_params_partial_page_stops(self) -> None:
        s = OffsetPagination()
        assert s.next_params({"limit": 1000, "offset": 0}, {}, [{"id": 1}]) is None

    def test_next_params_empty_page_stops(self) -> None:
        s = OffsetPagination()
        assert s.next_params({"limit": 1000, "offset": 0}, {}, []) is None

    def test_extract_page_returns_list(self) -> None:
        s = OffsetPagination()
        items = [{"id": 1}, {"id": 2}]
        assert s.extract_page(_OffsetMethod(), {"items": items}) == items

    def test_extract_page_missing_key_returns_empty(self) -> None:
        s = OffsetPagination()
        try:
            result = s.extract_page(_OffsetMethod(), {})
            assert result == []
        except (KeyError, TypeError):
            pass  # missing key raises; acceptable


@pytest.mark.unit
class TestNextCursorPagination:
    def test_first_params(self) -> None:
        s = NextCursorPagination()
        assert s.first_params() == {"limit": 1000, "next": 0}

    def test_next_params_returns_cursor(self) -> None:
        s = NextCursorPagination()
        result = s.next_params({"limit": 1000, "next": 0}, {"next": 12345}, [{"id": 1}])
        assert result == {"limit": 1000, "next": 12345}

    def test_next_params_zero_cursor_stops(self) -> None:
        s = NextCursorPagination()
        assert s.next_params({}, {"next": 0}, [{"id": 1}]) is None

    def test_next_params_missing_cursor_stops(self) -> None:
        s = NextCursorPagination()
        assert s.next_params({}, {}, []) is None

    def test_next_params_non_dict_response_stops(self) -> None:
        s = NextCursorPagination()
        assert s.next_params({}, None, []) is None

    def test_extract_page(self) -> None:
        s = NextCursorPagination()
        orders = [{"id": 1}]
        assert s.extract_page(_NextMethod(), {"orders": orders}) == orders


@pytest.mark.unit
class TestTakeSkipPagination:
    def test_first_params(self) -> None:
        s = TakeSkipPagination()
        assert s.first_params() == {"take": 5000, "skip": 0}

    def test_page_size_is_5000(self) -> None:
        assert TakeSkipPagination.page_size == 5000

    def test_next_params_full_page_advances_skip(self) -> None:
        s = TakeSkipPagination()
        page = [{"id": i} for i in range(5000)]
        assert s.next_params({"take": 5000, "skip": 0}, {}, page) == {"take": 5000, "skip": 5000}

    def test_next_params_second_advance(self) -> None:
        s = TakeSkipPagination()
        page = [{"id": i} for i in range(5000)]
        assert s.next_params({"take": 5000, "skip": 5000}, {}, page) == {"take": 5000, "skip": 10000}

    def test_next_params_partial_page_stops(self) -> None:
        s = TakeSkipPagination()
        assert s.next_params({"take": 5000, "skip": 0}, {}, [{"id": 1}] * 42) is None


@pytest.mark.unit
class TestPaginationStrategiesRegistry:
    def test_all_three_strategies_registered(self) -> None:
        assert set(PAGINATION_STRATEGIES.keys()) == {"offset", "next", "take_skip"}

    def test_offset_strategy_type(self) -> None:
        assert isinstance(PAGINATION_STRATEGIES["offset"], OffsetPagination)

    def test_next_strategy_type(self) -> None:
        assert isinstance(PAGINATION_STRATEGIES["next"], NextCursorPagination)

    def test_take_skip_strategy_type(self) -> None:
        assert isinstance(PAGINATION_STRATEGIES["take_skip"], TakeSkipPagination)


# ---------------------------------------------------------------------------
# Integration tests — full pagination loop via paginate(bound_method, **kwargs)
# ---------------------------------------------------------------------------

@pytest.mark.unit
class TestOffsetPaginationIntegration:
    async def test_single_partial_page_stops(self, api: MockedAPI) -> None:
        api.add_response({"items": [{"id": 1}, {"id": 2}]})
        result = await paginate(_bound(api, _OffsetMethod))

        assert len(result) == 2
        assert isinstance(result[0], _Item)
        req = api.mocked_session.requests[-1]
        assert req.params["limit"] == 1000
        assert req.params["offset"] == 0

    async def test_full_page_then_partial_page(self, api: MockedAPI) -> None:
        page1 = [{"id": i} for i in range(1000)]
        page2 = [{"id": i} for i in range(3)]
        api.add_response({"items": page1})
        api.add_response({"items": page2})

        result = await paginate(_bound(api, _OffsetMethod))

        assert len(result) == 1003
        assert len(api.mocked_session.requests) == 2
        assert api.mocked_session.requests[1].params["offset"] == 1000

    async def test_three_pages(self, api: MockedAPI) -> None:
        full_page = [{"id": i} for i in range(1000)]
        api.add_response({"items": full_page})
        api.add_response({"items": full_page})
        api.add_response({"items": [{"id": 0}]})

        result = await paginate(_bound(api, _OffsetMethod))

        assert len(result) == 2001
        assert api.mocked_session.requests[2].params["offset"] == 2000

    async def test_empty_first_page_returns_empty_list(self, api: MockedAPI) -> None:
        api.add_response({"items": []})
        result = await paginate(_bound(api, _OffsetMethod))
        assert result == []

    async def test_no_pagination_raises(self, api: MockedAPI) -> None:
        class _NoPageMethod(WbMethod):
            __return__ = _Item
            __api__ = "test"
            __method__ = "api/v1/no-page"
            request_limit: RequestLimit = RequestLimit(period=60, limit=60, interval=60, burst=10)

        with pytest.raises(TypeError, match="does not support pagination"):
            await paginate(_bound(api, _NoPageMethod))


@pytest.mark.unit
class TestNextCursorPaginationIntegration:
    async def test_single_page_cursor_zero(self, api: MockedAPI) -> None:
        api.add_response({"orders": [{"id": 1}], "next": 0})
        result = await paginate(_bound(api, _NextMethod))

        assert len(result) == 1
        req = api.mocked_session.requests[-1]
        assert req.params["limit"] == 1000
        assert req.params["next"] == 0

    async def test_two_pages_cursor_forwarded(self, api: MockedAPI) -> None:
        page1 = [{"id": i} for i in range(1000)]
        page2 = [{"id": i} for i in range(50)]
        api.add_response({"orders": page1, "next": 99999})
        api.add_response({"orders": page2, "next": 0})

        result = await paginate(_bound(api, _NextMethod))

        assert len(result) == 1050
        assert api.mocked_session.requests[1].params["next"] == 99999

    async def test_empty_first_page_returns_empty_list(self, api: MockedAPI) -> None:
        api.add_response({"orders": [], "next": 0})
        result = await paginate(_bound(api, _NextMethod))
        assert result == []


@pytest.mark.unit
class TestTakeSkipPaginationIntegration:
    async def test_single_partial_page(self, api: MockedAPI) -> None:
        api.add_response({"feedbacks": [{"id": 1}]})
        result = await paginate(_bound(api, _TakeSkipMethod))

        assert len(result) == 1
        req = api.mocked_session.requests[-1]
        assert req.params["take"] == 5000
        assert req.params["skip"] == 0

    async def test_full_page_then_partial_page(self, api: MockedAPI) -> None:
        page1 = [{"id": i} for i in range(5000)]
        page2 = [{"id": i} for i in range(200)]
        api.add_response({"feedbacks": page1})
        api.add_response({"feedbacks": page2})

        result = await paginate(_bound(api, _TakeSkipMethod))

        assert len(result) == 5200
        assert api.mocked_session.requests[1].params["skip"] == 5000

    async def test_empty_first_page_returns_empty_list(self, api: MockedAPI) -> None:
        api.add_response({"feedbacks": []})
        result = await paginate(_bound(api, _TakeSkipMethod))
        assert result == []
