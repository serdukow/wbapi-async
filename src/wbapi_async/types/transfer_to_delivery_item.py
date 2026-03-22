from typing import Any

from pydantic import Field

from .base import BaseType


class TransferToDeliveryItem(BaseType):
    """Transfer to Delivery"""

    errors: list[Any] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
