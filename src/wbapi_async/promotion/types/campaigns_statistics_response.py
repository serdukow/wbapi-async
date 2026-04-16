from pydantic import Field

from ...types.base import BaseType
from .booster_stats_item import BoosterStatsItem
from .days_item import DaysItem


class CampaignsStatisticsResponse(BaseType):
    """Campaigns Statistics"""

    advert_id: int = Field(alias="advertId")
    atbs: int = Field(alias="atbs")
    booster_stats: list[BoosterStatsItem] | None = Field(None, alias="boosterStats")
    canceled: int = Field(alias="canceled")
    clicks: int = Field(alias="clicks")
    cpc: float = Field(alias="cpc")
    cr: float = Field(alias="cr")
    ctr: float = Field(alias="ctr")
    days: list[DaysItem] = Field(alias="days")
    orders: int = Field(alias="orders")
    shks: int = Field(alias="shks")
    sum_: float = Field(alias="sum")
    sum_price: float = Field(alias="sum_price")
    views: int = Field(alias="views")
