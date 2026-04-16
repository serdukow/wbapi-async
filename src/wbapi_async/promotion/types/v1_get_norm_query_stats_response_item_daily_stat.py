from pydantic import Field

from ...types.base import BaseType
from .v1_get_norm_query_stats_response_item_stat import V1GetNormQueryStatsResponseItemStat


class V1GetNormQueryStatsResponseItemDailyStat(BaseType):
    date: str = Field()
    stat: V1GetNormQueryStatsResponseItemStat | None = Field(None)
