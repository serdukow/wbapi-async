from __future__ import annotations

from collections.abc import AsyncIterator
import copy
import re
from typing import TYPE_CHECKING, Any, ClassVar, Generic, TypeVar

import msgspec

from ..exceptions import WBConfigurationError, WBDecodeError
from .model import WBModel, collect_extras


if TYPE_CHECKING:
    from .api import WBApi

_UNSAFE = re.compile(r"[/?#%\\\s]|\.\.")
_SHAPE_MISMATCH = re.compile(r"Expected `(?P<want>[\w| ]+)`, got `(?P<got>\w+)` - at `\$\.(?P<path>[\w.]+)`")

MAX_PAGES = 10_000

T = TypeVar("T")


class WBMethod(msgspec.Struct, Generic[T], omit_defaults=True, kw_only=True):
    if TYPE_CHECKING:
        __path__: ClassVar[str]
        __http_method__: ClassVar[str]
        __returns__: ClassVar[type | None]
        __path_params__: ClassVar[tuple[str, ...]]
        __query_params__: ClassVar[dict[str, str]]
        __body_fields__: ClassVar[dict[str, str]]
        __paginate__: ClassVar[str | None]
        __items__: ClassVar[str | None]
        __host__: ClassVar[str]
        __sandbox_host__: ClassVar[str]
        __rate_limits__: ClassVar[dict[str, tuple[int, int]]]

    def url(self, sandbox: bool = False) -> str:
        if not sandbox:
            return f"{self.__host__}{self._path()}"

        host = getattr(self, "__sandbox_host__", "")
        if not host:
            raise WBConfigurationError(
                f"{self.__http_method__} {self.__path__}: у метода нет песочницы. "
                f"См. https://dev.wildberries.ru/sandbox"
            )
        return f"{host}{self._path()}"

    def _path(self) -> str:
        path = self.__path__
        for name in getattr(self, "__path_params__", ()):
            value = str(getattr(self, _attr(name)))
            # A value with .. or / would silently retarget the request.
            if _UNSAFE.search(value):
                raise ValueError(f"Недопустимое значение {name}={value!r} в пути запроса")
            path = path.replace(f"{{{name}}}", value)
        return path

    def _query(self, extra: dict[str, Any] | None = None) -> dict[str, Any] | None:
        query = {
            api_name: value
            for attr, api_name in getattr(self, "__query_params__", {}).items()
            if (value := getattr(self, attr, None)) is not None
        }
        query.update(extra or {})
        return query or None

    def _body(self, extra: dict[str, Any] | None = None) -> Any:
        fields = getattr(self, "__body_fields__", None)
        if not fields:
            body = getattr(self, "body", None)
            if not extra:
                return body
            # Pagination keys must survive even when the method has no body.
            return {**body, **extra} if isinstance(body, dict) else dict(extra)
        body = {
            api_name: msgspec.to_builtins(value)
            for attr, api_name in fields.items()
            if (value := getattr(self, attr, None)) is not None
        }
        body.update(extra or {})
        return body or None

    def rate_limit(self, kind: str | None) -> tuple[int, int] | None:
        limits: dict[str, tuple[int, int]] = getattr(self, "__rate_limits__", {})
        if not limits:
            return None
        if kind and kind in limits:
            return limits[kind]
        for fallback in ("all", "personal", "service"):
            if fallback in limits:
                return limits[fallback]
        return next(iter(limits.values()))

    def _decode(self, raw: Any) -> T:
        returns = getattr(self, "__returns__", None)
        if returns is None or raw is None:
            return None  # type: ignore[return-value]
        try:
            # strict=False accepts harmless drift: numbers as strings, int for float.
            decoded: T = msgspec.convert(raw, returns, strict=False)
            _keep_extras(raw, decoded)
            return decoded
        except msgspec.ValidationError as exc:
            relaxed = _relax_shape(raw, str(exc))
            if relaxed is not None:
                try:
                    fallback: T = msgspec.convert(relaxed, returns, strict=False)
                    _keep_extras(relaxed, fallback)
                    return fallback
                except msgspec.ValidationError:
                    pass
            raise WBDecodeError(
                f"{self.__http_method__} {self.__path__}: ответ не совпал с описанием "
                f"в спецификации — {exc}. Обновите спецификации "
                f"(uv run python scripts/update_specs.py) и перегенерируйте клиент.",
                path=self.__path__,
                payload=raw,
            ) from exc

    async def emit(self, api: WBApi) -> T:
        raw = await api._send(self, params=self._query(), json=self._body())
        return self._decode(raw)

    async def stream(self, api: WBApi) -> AsyncIterator[Any]:
        scheme = getattr(self, "__paginate__", None)
        items = getattr(self, "__items__", None)

        if scheme is None:
            for item in _rows(await self.emit(api), items):
                yield item
            return

        walk = getattr(self, f"_walk_{scheme}")
        pages = 0
        async for raw in walk(api):
            pages += 1
            if pages > MAX_PAGES:
                raise RuntimeError(f"Обход превысил {MAX_PAGES} страниц; прерываю")
            for item in _rows(self._decode(raw), items):
                yield item

    async def paginate(self, api: WBApi) -> list[Any]:
        return [item async for item in self.stream(api)]

    async def _walk_next(self, api: WBApi) -> AsyncIterator[Any]:
        cursor: Any = None
        seen: set[Any] = set()
        while True:
            extra = {"next": cursor} if cursor is not None else {}
            raw = await api._send(self, params=self._query(extra), json=self._body())
            yield raw
            cursor = raw.get("next") if isinstance(raw, dict) else None
            # A repeated cursor means the server stopped advancing.
            if not cursor or cursor in seen:
                return
            if not _rows(self._decode(raw), getattr(self, "__items__", None)):
                return
            seen.add(cursor)

    async def _walk_skip_take(self, api: WBApi) -> AsyncIterator[Any]:
        take = getattr(self, "take", None) or 5000
        skip = 0
        while True:
            raw = await api._send(self, params=self._query({"skip": skip, "take": take}), json=self._body())
            yield raw
            if len(_rows(self._decode(raw), getattr(self, "__items__", None))) < take:
                return
            skip += take

    async def _walk_offset_query(self, api: WBApi) -> AsyncIterator[Any]:
        limit = getattr(self, "limit", None) or 1000
        offset = 0
        while True:
            raw = await api._send(
                self,
                params=self._query({"offset": offset, "limit": limit}),
                json=self._body(),
            )
            yield raw
            if len(_rows(self._decode(raw), getattr(self, "__items__", None))) < limit:
                return
            offset += limit

    async def _walk_offset_body(self, api: WBApi) -> AsyncIterator[Any]:
        limit = getattr(self, "limit", None) or 1000
        offset = 0
        while True:
            raw = await api._send(
                self,
                params=self._query(),
                json=self._body({"offset": offset, "limit": limit}),
            )
            yield raw
            if len(_rows(self._decode(raw), getattr(self, "__items__", None))) < limit:
                return
            offset += limit

    async def _walk_cursor(self, api: WBApi) -> AsyncIterator[Any]:
        limit = getattr(self, "limit", None) or 100
        cursor: dict[str, Any] = {"limit": limit}
        while True:
            body = self._body() or {}
            settings = body.get("settings") if isinstance(body, dict) else None
            merged = {**body, "settings": {**(settings or {}), "cursor": cursor}}
            raw = await api._send(self, params=self._query(), json=merged)
            yield raw
            got = raw.get("cursor") if isinstance(raw, dict) else None
            if not isinstance(got, dict) or got.get("total", 0) < limit:
                return
            if "updatedAt" not in got or "nmID" not in got:
                return
            cursor = {"limit": limit, "updatedAt": got["updatedAt"], "nmID": got["nmID"]}

    async def _walk_rrdid(self, api: WBApi) -> AsyncIterator[Any]:
        rrd_id: Any = None
        seen: set[Any] = set()
        while True:
            extra = {"rrdId": rrd_id} if rrd_id is not None else {}
            raw = await api._send(self, params=self._query(), json=self._body(extra))
            yield raw
            rows = _rows(self._decode(raw), getattr(self, "__items__", None))
            if not rows:
                return
            rrd_id = getattr(rows[-1], "rrd_id", None)
            if not rrd_id or rrd_id in seen:
                return
            seen.add(rrd_id)


def _keep_extras(raw: Any, decoded: Any) -> None:
    try:
        if isinstance(decoded, list):
            if isinstance(raw, list):
                for source, item in zip(raw, decoded, strict=False):
                    _keep_extras(source, item)
            return

        if not isinstance(decoded, WBModel) or not isinstance(raw, dict):
            return

        found = collect_extras(raw, type(decoded))
        if found:
            decoded.extras = found
    except Exception:
        return


def _relax_shape(raw: Any, message: str) -> Any:
    match = _SHAPE_MISMATCH.search(message)
    if not match or not isinstance(raw, dict):
        return None

    parts = match["path"].split(".")
    node: Any = raw
    for part in parts[:-1]:
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    key = parts[-1]
    if not isinstance(node, dict) or key not in node:
        return None

    value = node[key]
    want, got = match["want"], match["got"]
    if got == "array" and "object" in want and isinstance(value, list):
        replacement = value[0] if value else None
    elif got == "object" and "array" in want and isinstance(value, dict):
        replacement = [value]
    else:
        return None

    patched = copy.deepcopy(raw)
    node = patched
    for part in parts[:-1]:
        node = node[part]
    node[key] = replacement
    return patched


def _rows(page: Any, items_field: str | None) -> list[Any]:
    if page is None:
        return []
    if isinstance(page, list):
        return page
    if items_field:
        rows = getattr(page, _attr(items_field), None)
        if isinstance(rows, list):
            return rows
        if isinstance(rows, msgspec.Struct):
            nested = _rows(rows, None)
            if nested:
                return nested
    if isinstance(page, msgspec.Struct):
        fields = msgspec.structs.asdict(page)
        for value in fields.values():
            if isinstance(value, list):
                return value
        # Rows sometimes sit one level deeper, e.g. under data.feedbacks.
        for value in fields.values():
            if isinstance(value, msgspec.Struct):
                nested = _rows(value, None)
                if nested:
                    return nested
    return []


def _attr(api_name: str) -> str:
    out = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", api_name)
    return re.sub(r"[^a-zA-Z0-9]+", "_", out).lower().strip("_")
