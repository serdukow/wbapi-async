from typing import Any

from pydantic import Field

from ...types import DailySearchClustersStatisticsItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class DailySearchClustersStatistics(WbMethod):
    """
    Returns statistics (views, clicks, add-to-cart, orders, CTR, CPC, CPM, etc.) by search clusters
    forthe specified period detailed by day. Request limit per one seller's account:

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v1~1normquery~1stats/post
    """

    __return__ = DailySearchClustersStatisticsItem
    __api__ = "advert-api"
    __method__ = "adv/v1/normquery/stats"
    __http_method__ = "POST"
    __data_key__ = "items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    from_: str = Field(alias="from")
    to: str = Field()
    items: list[dict[str, Any]] = Field()
