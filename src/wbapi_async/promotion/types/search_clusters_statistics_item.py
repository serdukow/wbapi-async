from pydantic import Field

from ...types.base import BaseType
from .v0_get_norm_query_stats_item_stat import V0GetNormQueryStatsItemStat


class SearchClustersStatisticsItem(BaseType):
    """Search Clusters Statistics"""

    advert_id: int = Field(alias="advert_id")
    nm_id: int = Field(alias="nm_id")
    stats: list[V0GetNormQueryStatsItemStat] | None = Field(None, alias="stats")
