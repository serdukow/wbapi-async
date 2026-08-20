from __future__ import annotations

import sys
from typing import Any


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

import msgspec


__all__ = ("WBModel",)


class WBModel(msgspec.Struct, omit_defaults=True):
    def to_dict(self, *, by_alias: bool = False, skip_none: bool = True) -> dict[str, Any]:
        if by_alias:
            data: dict[str, Any] = msgspec.to_builtins(self)
            return data
        raw = msgspec.structs.asdict(self)
        items = ((k, _plain(v)) for k, v in raw.items())
        return {k: v for k, v in items if not skip_none or v is not None}

    def to_json(self, *, by_alias: bool = True) -> bytes:
        return msgspec.json.encode(self if by_alias else self.to_dict())

    @classmethod
    def from_dict(cls, data: Any) -> Self:
        return msgspec.convert(data, cls, strict=False)


def _plain(value: Any) -> Any:
    if isinstance(value, WBModel):
        return value.to_dict()
    if isinstance(value, msgspec.Struct):
        return msgspec.structs.asdict(value)
    if isinstance(value, list):
        return [_plain(item) for item in value]
    if isinstance(value, dict):
        return {key: _plain(item) for key, item in value.items()}
    return value
