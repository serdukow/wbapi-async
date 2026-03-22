from typing import Any

from pydantic import Field

from .base import BaseType


class NotifyThatTheOrdersWereReceivedByTheBuyersItem(BaseType):
    """Notify That the Orders Were Received by the Buyers"""

    order_id: int = Field(None, alias="orderId")
    is_error: bool = Field(None, alias="isError")
    errors: list[Any] | None = Field(None)
