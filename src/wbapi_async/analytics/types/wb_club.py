from pydantic import Field

from ...types.base import BaseType


class WbClub(BaseType):
    order_count: int = Field(alias="orderCount")
    order_sum: int = Field(alias="orderSum")
    buyout_sum: int = Field(alias="buyoutSum")
    buyout_count: int = Field(alias="buyoutCount")
    cancel_sum: int = Field(alias="cancelSum")
    cancel_count: int = Field(alias="cancelCount")
    avg_price: int = Field(alias="avgPrice")
    buyout_percent: int = Field(alias="buyoutPercent")
    avg_order_count_per_day: float = Field(alias="avgOrderCountPerDay")
