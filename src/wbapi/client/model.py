from __future__ import annotations

import sys
import types
import typing
from typing import Any, get_args, get_origin


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

import msgspec


__all__ = ("WBModel",)

STORAGE = "extras"
_STORAGE_ALIAS = "__extras__"


class WBModel(msgspec.Struct, omit_defaults=True):
    extras: dict[str, Any] | None = msgspec.field(default=None, name=_STORAGE_ALIAS)

    def to_dict(
        self, *, by_alias: bool = False, skip_none: bool = True, extra: bool = False
    ) -> dict[str, Any]:
        if by_alias:
            data: dict[str, Any] = msgspec.to_builtins(self)
        else:
            raw = msgspec.structs.asdict(self)
            items = ((k, _plain(v, extra)) for k, v in raw.items())
            data = {k: v for k, v in items if not skip_none or v is not None}

        data.pop(STORAGE, None)
        data.pop(_STORAGE_ALIAS, None)
        if extra and self.extras:
            return _merge(data, self.extras)
        return data

    def to_json(self, *, by_alias: bool = True, extra: bool = False) -> bytes:
        return msgspec.json.encode(self.to_dict(by_alias=by_alias, extra=extra))

    @classmethod
    def from_dict(cls, data: Any) -> Self:
        return msgspec.convert(data, cls, strict=False)


def _merge(data: dict[str, Any], unknown: dict[str, Any]) -> dict[str, Any]:
    merged = dict(data)
    for key, value in unknown.items():
        current = merged.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            merged[key] = _merge(current, value)
        elif isinstance(current, list) and isinstance(value, list):
            merged[key] = [
                _merge(item, found) if isinstance(item, dict) and isinstance(found, dict) else item
                for item, found in zip(current, value, strict=False)
            ]
        elif key not in merged:
            merged[key] = value
    return merged


def _plain(value: Any, extra: bool = False) -> Any:
    if isinstance(value, WBModel):
        return value.to_dict(extra=extra)
    if isinstance(value, msgspec.Struct):
        return msgspec.structs.asdict(value)
    if isinstance(value, list):
        return [_plain(item, extra) for item in value]
    if isinstance(value, dict):
        return {key: _plain(item, extra) for key, item in value.items()}
    return value


_plans: dict[type, tuple[frozenset[str], dict[str, type]]] = {}


def _struct_of(annotation: Any) -> type | None:
    origin = get_origin(annotation)

    if origin in (typing.Union, types.UnionType):
        for arg in get_args(annotation):
            if arg is not type(None):
                found = _struct_of(arg)
                if found is not None:
                    return found
        return None

    if origin in (list, set, tuple, frozenset):
        args = get_args(annotation)
        return _struct_of(args[0]) if args else None

    if isinstance(annotation, type) and issubclass(annotation, msgspec.Struct):
        return annotation

    return None


def _plan(struct: type) -> tuple[frozenset[str], dict[str, type]]:
    plan = _plans.get(struct)
    if plan is not None:
        return plan

    hints = typing.get_type_hints(struct)
    fields = [f for f in msgspec.structs.fields(struct) if f.name != STORAGE]
    known = frozenset(f.encode_name for f in fields)
    nested = {}
    for field in fields:
        inner = _struct_of(hints.get(field.name))
        if inner is not None:
            nested[field.encode_name] = inner

    plan = (known, nested)
    _plans[struct] = plan
    return plan


def collect_extras(raw: Any, struct: type | None) -> Any:
    if struct is None:
        return None

    if isinstance(raw, list):
        found = [collect_extras(item, struct) for item in raw]
        return found if any(item is not None for item in found) else None

    if not isinstance(raw, dict):
        return None

    known, nested = _plan(struct)
    extras: dict[str, Any] | None = None

    for key, value in raw.items():
        if key not in known:
            if extras is None:
                extras = {}
            extras[key] = value
            continue

        inner = nested.get(key)
        if inner is None:
            continue

        deeper = collect_extras(value, inner)
        if deeper:
            if extras is None:
                extras = {}
            extras[key] = deeper

    return extras
