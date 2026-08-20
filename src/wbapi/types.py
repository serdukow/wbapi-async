"""Response objects: real ``dict`` and ``list`` subclasses with attribute access.

A decoded response behaves exactly like the plain Python structure it came
from — it serialises with ``json.dumps``, unpacks with ``{**item}``, and passes
``isinstance`` checks — while also allowing ``response.orders[0].nmID``.
"""

from __future__ import annotations

from typing import Any


__all__ = ("WBObject", "WBDict", "WBList")

_MAX_REPR_LEN = 200


def wrap(value: Any) -> Any:
    """Wrap containers so nested access keeps working; leave scalars alone."""
    if type(value) is dict:
        return WBDict(value)
    if type(value) is list:
        return WBList(value)
    return value


class WBObject:
    """Base for :class:`WBDict` and :class:`WBList`."""

    __slots__ = ()


class WBDict(dict[str, Any], WBObject):
    """A JSON object: a ``dict`` that also answers to attribute access.

    Example::

        resp = await api.get("/api/v3/orders/new")
        resp.orders[0].nmID
        json.dumps(resp)
    """

    __slots__ = ()

    def __getattr__(self, name: str) -> Any:
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        try:
            value = dict.__getitem__(self, name)
        except KeyError:
            available = ", ".join(map(str, self)) or "<empty>"
            raise AttributeError(f"{name!r} not found. Response contains: {available}") from None
        return wrap(value)

    def __getitem__(self, key: str) -> Any:
        return wrap(dict.__getitem__(self, key))

    def get(self, key: str, default: Any = None) -> Any:
        if key in self:
            return wrap(dict.__getitem__(self, key))
        return default

    def values(self) -> Any:
        return [wrap(v) for v in dict.values(self)]

    def items(self) -> Any:
        return [(k, wrap(v)) for k, v in dict.items(self)]

    def __repr__(self) -> str:
        body = dict.__repr__(self)
        if len(body) > _MAX_REPR_LEN:
            body = body[:_MAX_REPR_LEN] + "…"
        return body


class WBList(list[Any], WBObject):
    """A JSON array: a ``list`` whose items are wrapped on access.

    Example::

        supplies = await api.get("/api/v3/supplies")
        supplies[0].id
        sorted(supplies, key=lambda s: s.id)
    """

    __slots__ = ()

    def __getitem__(self, index: Any) -> Any:
        value = list.__getitem__(self, index)
        return WBList(value) if isinstance(index, slice) else wrap(value)

    def __iter__(self) -> Any:
        return (wrap(v) for v in list.__iter__(self))

    def __getattr__(self, name: str) -> Any:
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        raise AttributeError(
            f"{name!r} not found: this is a list of {len(self)} items. "
            f"Iterate it, or index it first — e.g. response[0].{name}"
        )

    def __repr__(self) -> str:
        body = list.__repr__(self)
        if len(body) > _MAX_REPR_LEN:
            body = body[:_MAX_REPR_LEN] + "…"
        return body
