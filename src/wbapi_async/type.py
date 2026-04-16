from __future__ import annotations

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
            raise AttributeError(name) from None
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
