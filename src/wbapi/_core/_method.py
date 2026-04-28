from __future__ import annotations

from typing import Any

from ..type import WBType, _wrap
from ._registry import _PAGE_SIZES, _PUBLIC
from ._session import BaseSession
from .limiter import _get_limiter
from .paginate import fetch_all
from .parse_url import parse_url


class MethodDispatcher:
    def __init__(self, session: BaseSession, token: str) -> None:
        self._session = session
        self._token = token

    async def dispatch(
        self,
        http_method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
        paginate: bool = False,
        no_auth: bool = False,
    ) -> Any:
        import re
        from urllib.parse import urlparse

        placeholders = re.findall(r"\{(\w+)\}", path)
        if placeholders and params:
            params = dict(params)
            for key in placeholders:
                if key in params:
                    path = path.replace(f"{{{key}}}", str(params.pop(key)))
            params = params or None

        if not no_auth and path.startswith(("https://", "http://")):
            no_auth = urlparse(path).netloc in _PUBLIC

        if no_auth:
            self._session.headers.authorization = None
        else:
            self._session.headers.set_token(self._token)

        if paginate:
            page_size = _PAGE_SIZES.get(path, 1000)

            async def _request(
                params: dict[str, Any] | None = None,
                body: dict[str, Any] | None = None,
            ) -> Any:
                url = parse_url(path)
                limiter = _get_limiter(path)
                return await self._session._request(http_method, url, params=params, json=body, limit=limiter)

            return [WBType(item) for item in await fetch_all(_request, path, page_size, params, json)]

        url = parse_url(path)
        limiter = _get_limiter(path)
        return _wrap(await self._session._request(http_method, url, params=params, json=json, limit=limiter))
