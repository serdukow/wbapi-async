from typing import Any

from pydantic import Field

from ...types.base import BaseType


class DailySearchClustersStatisticsItem(BaseType):
    """Daily Search Clusters Statistics"""

    advert_id: int = Field(alias="advertId")
    nm_id: int = Field(alias="nmId")
    daily_stats: list[Any] | None = Field(None, alias="dailyStats")
