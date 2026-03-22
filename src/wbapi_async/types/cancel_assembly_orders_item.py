from typing import Any

from pydantic import Field

from .base import BaseType


class CancelAssemblyOrdersItem(BaseType):
    """Cancel Assembly Orders"""

    errors: list[Any] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
