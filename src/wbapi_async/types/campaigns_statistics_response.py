from typing import Any

from pydantic import Field

from .base import BaseType


class CampaignsStatisticsResponse(BaseType):
    """Campaigns Statistics"""

    advert_id: int = Field(None, alias="advertId")
    atbs: int = Field(None)
    booster_stats: Any | None = Field(None, alias="boosterStats")
    canceled: int = Field(None)
    clicks: int = Field(None)
    cpc: float = Field(None)
    cr: float = Field(None)
    ctr: float = Field(None)
    days: Any = Field(None)
    orders: int = Field(None)
    shks: int = Field(None)
    sum: float = Field(None)
    sum_price: float = Field(None)
    views: int = Field(None)
