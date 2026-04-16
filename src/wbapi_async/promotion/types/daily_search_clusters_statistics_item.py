from pydantic import Field

from ...types.base import BaseType
from .v1_get_norm_query_stats_response_item_daily_stat import V1GetNormQueryStatsResponseItemDailyStat


class DailySearchClustersStatisticsItem(BaseType):
    """Daily Search Clusters Statistics"""

    advert_id: int = Field(alias="advertId")
    nm_id: int = Field(alias="nmId")
    daily_stats: list[V1GetNormQueryStatsResponseItemDailyStat] | None = Field(None, alias="dailyStats")
