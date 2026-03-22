from typing import Any

from pydantic import Field

from ...types.base import BaseType


class StatusHistoryForCrossborderOrdersItem(BaseType):
    """Status History for Cross-Border Orders"""

    delivery_date: str | None = Field(None, alias="deliveryDate")
    statuses: list[dict[str, Any]] | None = Field(None)
    order_id: int | None = Field(None, alias="orderID")
