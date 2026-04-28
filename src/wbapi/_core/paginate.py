from __future__ import annotations

from collections.abc import Callable
from typing import Any

from ._paginators import _extract_list, detect_and_paginate


_Requester = Callable[..., Any]


async def fetch_all(
    request: _Requester,
    path: str,
    page_size: int,
    params: dict[str, Any] | None,
    body: dict[str, Any] | None,
) -> list[Any]:
    init_params = {**(params or {}), "limit": page_size}
    if body is not None:
        init_body = {**body}
        raw = await request(params=init_params or None, body=init_body)
    else:
        raw = await request(params=init_params)

    page = _extract_list(raw) or []
    return await detect_and_paginate(raw, page, request, init_params, body, page_size)
