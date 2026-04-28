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
    if body is not None:
        raw = await request(params=params or None, body=body)
        page = _extract_list(raw) or []
        return await detect_and_paginate(raw, page, request, {}, body, page_size)
    else:
        init_params = {**(params or {}), "limit": page_size}
        raw = await request(params=init_params)
        page = _extract_list(raw) or []
        return await detect_and_paginate(raw, page, request, init_params, None, page_size)
