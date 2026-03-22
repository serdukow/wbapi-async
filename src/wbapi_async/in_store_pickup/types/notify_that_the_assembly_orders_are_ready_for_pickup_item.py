from typing import Any

from pydantic import Field

from ...types.base import BaseType


class NotifyThatTheAssemblyOrdersAreReadyForPickupItem(BaseType):
    """Notify That the Assembly Orders Are Ready for Pickup"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[Any] | None = Field(None)
