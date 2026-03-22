from typing import Any

from pydantic import Field

from .base import BaseType


class AddGtinToAssemblyOrdersItem(BaseType):
    """Add GTIN to Assembly Orders"""

    errors: list[Any] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
