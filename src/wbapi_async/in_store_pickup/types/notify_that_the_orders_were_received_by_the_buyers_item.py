from typing import Any

from pydantic import Field

from ...types.base import BaseType


class NotifyThatTheOrdersWereReceivedByTheBuyersItem(BaseType):
    """Notify That the Orders Were Received by the Buyers"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[Any] | None = Field(None)
