from typing import Any

from pydantic import Field

from .base import BaseType


class AcceptanceOptionsItem(BaseType):
    """Acceptance Options"""

    barcode: str | None = Field(None)
    error: dict[str, Any] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    warehouses: list[dict[str, Any]] | None = Field(None)
