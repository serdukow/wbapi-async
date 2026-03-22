from typing import Any

from pydantic import Field

from .base import BaseType


class DailySearchClustersStatisticsItem(BaseType):
    """Daily Search Clusters Statistics"""

    advert_id: int = Field(None, alias="advertId")
    nm_id: int = Field(None, alias="nmId")
    daily_stats: list[Any] | None = Field(None, alias="dailyStats")
