from typing import Any

from pydantic import Field

from ...types.base import BaseType


class CampaignsStatisticsResponse(BaseType):
    """Campaigns Statistics"""

    advert_id: int = Field(alias="advertId")
    atbs: int = Field()
    booster_stats: Any | None = Field(None, alias="boosterStats")
    canceled: int = Field()
    clicks: int = Field()
    cpc: float = Field()
    cr: float = Field()
    ctr: float = Field()
    days: Any = Field()
    orders: int = Field()
    shks: int = Field()
    sum_: float = Field(alias="sum")
    sum_price: float = Field()
    views: int = Field()
