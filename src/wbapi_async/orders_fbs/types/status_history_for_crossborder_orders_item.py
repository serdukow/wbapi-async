from pydantic import Field

from ...types.base import BaseType
from .statuses_item import StatusesItem


class StatusHistoryForCrossborderOrdersItem(BaseType):
    """Status History for Cross-Border Orders"""

    delivery_date: str | None = Field(None, alias="deliveryDate")
    statuses: list[StatusesItem] | None = Field(None)
    order_id: int | None = Field(None, alias="orderID")
