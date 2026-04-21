from __future__ import annotations

import re
from typing import Any


def _wrap(val: Any) -> Any:
    return ApiResponse(val) if isinstance(val, (dict | list)) else val


class ApiResponse:
    __slots__ = ("_data",)

    def __init__(self, data: Any) -> None:
        self._data = data

    def __getattr__(self, name: str) -> Any:
        try:
            val = self._data[name]
        except (KeyError, TypeError):
            available = list(self._data) if isinstance(self._data, dict) else type(self._data).__name__
            raise AttributeError(f"{name!r} not found. Got: {available}") from None
        return _wrap(val)

    def __getitem__(self, key: str | int) -> Any:
        return _wrap(self._data[key])

    def __iter__(self) -> Any:
        if isinstance(self._data, list):
            return (_wrap(v) for v in self._data)
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return bool(self._data)

    def __repr__(self) -> str:
        return f"ApiResponse({self._data!r})"

    def unwrap(self) -> Any:
        return self._data

    def to_snake(self) -> dict[str, Any]:
        def convert(key: str) -> str:
            return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", key).lower()

        if isinstance(self._data, dict):
            return {convert(k): v for k, v in self._data.items()}
        return self._data
