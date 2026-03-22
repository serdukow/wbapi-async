from typing import Any

from pydantic import Field

from ..types.search_clusters_statistics_item import SearchClustersStatisticsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class SearchClustersStatistics(WbMethod):
    """
    The method returns statistics for search clusters over a specified period.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v0~1normquery~1stats/post
    """

    __return__ = SearchClustersStatisticsItem
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/stats"
    __http_method__ = "POST"
    __data_key__ = "stats"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=6, burst=20)

    from_: str = Field(None, alias="from")
    to: str = Field(None)
    items: list[dict[str, Any]] = Field(None)
