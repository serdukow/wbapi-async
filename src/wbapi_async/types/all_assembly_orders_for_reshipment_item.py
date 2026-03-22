from typing import Any

from pydantic import Field

from .base import BaseType


class AllAssemblyOrdersForReshipmentItem(BaseType):
    """Get All Assembly Orders for Re-shipment"""

    supply_id: Any | None = Field(None, alias="supplyID")
    order_id: Any | None = Field(None, alias="orderID")
