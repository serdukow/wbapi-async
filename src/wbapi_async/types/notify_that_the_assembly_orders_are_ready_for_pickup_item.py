from typing import Any

from pydantic import Field

from .base import BaseType


class NotifyThatTheAssemblyOrdersAreReadyForPickupItem(BaseType):
    """Notify That the Assembly Orders Are Ready for Pickup"""

    order_id: int = Field(None, alias="orderId")
    is_error: bool = Field(None, alias="isError")
    errors: list[Any] | None = Field(None)
