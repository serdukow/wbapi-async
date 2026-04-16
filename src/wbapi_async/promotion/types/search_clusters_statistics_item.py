from pydantic import Field

from ...types.base import BaseType
from .v0_get_norm_query_stats_item_stat import V0GetNormQueryStatsItemStat


class SearchClustersStatisticsItem(BaseType):
    """Search Clusters Statistics"""

    advert_id: int = Field()
    nm_id: int = Field()
    stats: list[V0GetNormQueryStatsItemStat] | None = Field(None)
