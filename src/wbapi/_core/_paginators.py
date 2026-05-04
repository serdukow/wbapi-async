from __future__ import annotations

from collections.abc import Callable
from typing import Any


_Requester = Callable[..., Any]


def _extract_list(raw: Any) -> list[Any] | None:
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        for v in raw.values():
            if isinstance(v, list):
                return v
        for v in raw.values():
            if isinstance(v, dict):
                found = _extract_list(v)
                if found is not None:
                    return found
    return None


async def next_token(
    raw: Any,
    page: list[Any],
    request: _Requester,
    params: dict[str, Any],
    page_size: int,
) -> list[Any]:
    """
    Token continuation pagination: API returns ``next`` in the response root,
    which is passed as ``?next=<value>`` in subsequent requests.

    Used by: Marketplace (FBS/DBS/DBW orders), Supplies FBW, Q&A, Reviews.
    Stop condition: ``next`` is falsy or the page is empty.
    """
    result: list[Any] = list(page)
    while True:
        cursor = raw.get("next") if isinstance(raw, dict) else None
        if not cursor or not page:
            break
        raw = await request(params={**params, "limit": page_size, "next": cursor})
        page = _extract_list(raw) or []
        result.extend(page)
    return result


async def rrdid_token(
    raw: Any,
    page: list[Any],
    request: _Requester,
    params: dict[str, Any],
    page_size: int,
) -> list[Any]:
    """
    Finance report token pagination (GET): last item has ``rrd_id``,
    passed as ``?rrdid=<value>`` in subsequent requests.

    Stop condition: page is empty (API returns 204 No Content → empty list).
    """
    result: list[Any] = list(page)
    while page:
        rrd_id = page[-1].get("rrd_id") if isinstance(page[-1], dict) else None
        if not rrd_id:
            break
        raw = await request(params={**params, "rrdid": rrd_id})
        page = _extract_list(raw) or []
        result.extend(page)
    return result


async def rrdid_post(
    raw: Any,
    page: list[Any],
    request: _Requester,
    body: dict[str, Any],
    page_size: int,
) -> list[Any]:
    """
    Finance report token pagination (POST body): last item has ``rrdId``,
    passed as ``"rrdId"`` in the request body for subsequent requests.

    Used by: Finance (/api/finance/v1/sales-reports/detailed).
    Stop condition: page is empty (API returns 204 No Content → empty list).
    """
    result: list[Any] = list(page)
    while len(page) >= page_size:
        last = page[-1]
        rrd_id = last.get("rrdId") if isinstance(last, dict) else None
        if not rrd_id:
            break
        raw = await request(body={**body, "rrdId": rrd_id})
        page = _extract_list(raw) or []
        result.extend(page)
    return result


async def offset(
    raw: Any,
    page: list[Any],
    request: _Requester,
    params: dict[str, Any],
    page_size: int,
) -> list[Any]:
    """
    Offset pagination: increments ``offset`` by ``limit`` each request.

    Used by: Analytics, Promotions, Reports.
    Stop condition: returned page is smaller than ``limit``.
    """
    result: list[Any] = list(page)
    current_offset = page_size
    while len(page) >= page_size:
        raw = await request(params={**params, "limit": page_size, "offset": current_offset})
        page = _extract_list(raw) or []
        result.extend(page)
        current_offset += page_size
    return result


async def offset_body(
    raw: Any,
    page: list[Any],
    request: _Requester,
    body: dict[str, Any],
    page_size: int,
) -> list[Any]:
    """
    Offset pagination via POST body: increments ``offset`` inside the request
    body by ``limit`` each request.

    Used by: Analytics v2 POST endpoints (e.g. /api/v2/stocks-report/products/products).
    Stop condition: returned page is smaller than ``limit``.
    """
    result: list[Any] = list(page)
    current_offset = page_size
    while len(page) >= page_size:
        raw = await request(body={**body, "limit": page_size, "offset": current_offset})
        page = _extract_list(raw) or []
        result.extend(page)
        current_offset += page_size
    return result


async def cursor(
    raw: Any,
    page: list[Any],
    request: _Requester,
    body: dict[str, Any],
    page_size: int,
) -> list[Any]:
    """
    Cursor pagination (POST body): API returns ``cursor`` object with
    ``updatedAt``, ``nmID``, and ``total``. Next request merges cursor
    fields into ``settings.cursor`` in the request body.

    Used by: Content v2 (cards list).
    Stop condition: ``cursor.total`` < ``limit``.
    """
    result: list[Any] = list(page)
    while True:
        cursor_obj = raw.get("cursor", {}) if isinstance(raw, dict) else {}
        total = cursor_obj.get("total", 0) if isinstance(cursor_obj, dict) else 0
        if total < page_size:
            break
        next_body = {
            **body,
            "settings": {
                **body.get("settings", {}),
                "cursor": {
                    "limit": page_size,
                    "updatedAt": cursor_obj["updatedAt"],
                    "nmID": cursor_obj["nmID"],
                },
            },
        }
        raw = await request(body=next_body)
        page = _extract_list(raw) or []
        result.extend(page)
    return result


def detect_and_paginate(
    raw: Any,
    page: list[Any],
    request: _Requester,
    params: dict[str, Any],
    body: dict[str, Any] | None,
    page_size: int,
) -> Any:
    """
    Auto-detect pagination type from first-page response and dispatch
    to the appropriate paginator coroutine.

    Detection order (first match wins):
    1. CursorPaginator        — POST body with ``cursor.updatedAt`` in response
    2. RrdIdPostPaginator     — POST body, last item has ``rrdId``
    3. NextTokenPaginator     — ``next`` key in response root
    4. RrdIdTokenPaginator    — last item in page has ``rrd_id`` (GET)
    5. OffsetBodyPaginator    — POST body, no cursor/rrdId match → offset in body
    6. OffsetPaginator        — fallback (GET offset via query params)
    """
    if body is not None and isinstance(raw, dict):
        cursor_obj = raw.get("cursor", {})
        if isinstance(cursor_obj, dict) and "updatedAt" in cursor_obj:
            return cursor(raw, page, request, body, page_size)

    if body is not None and page and isinstance(page[-1], dict) and "rrdId" in page[-1]:
        return rrdid_post(raw, page, request, body, page_size)

    if isinstance(raw, dict) and "next" in raw:
        return next_token(raw, page, request, params, page_size)

    if page and isinstance(page[-1], dict) and "rrd_id" in page[-1]:
        return rrdid_token(raw, page, request, params, page_size)

    if body is not None:
        return offset_body(raw, page, request, body, page_size)

    return offset(raw, page, request, params, page_size)
