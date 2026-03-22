from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AddGtinToTheAssemblyOrdersItem(BaseType):
    """Add GTIN to the Assembly Orders"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[Any] | None = Field(None)
