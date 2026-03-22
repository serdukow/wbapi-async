from typing import Any

from pydantic import Field

from .base import BaseType


class NotifyThatTheOrdersAreDeclinedItem(BaseType):
    """Notify that the Orders Are Declined"""

    order_id: int = Field(None, alias="orderId")
    is_error: bool = Field(None, alias="isError")
    errors: list[Any] | None = Field(None)
