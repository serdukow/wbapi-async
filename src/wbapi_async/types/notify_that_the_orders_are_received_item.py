from typing import Any

from pydantic import Field

from .base import BaseType


class NotifyThatTheOrdersAreReceivedItem(BaseType):
    """Notify that the Orders Are Received"""

    errors: list[dict[str, Any]] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
