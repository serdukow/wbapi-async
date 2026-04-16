from pydantic import Field

from ...methods.base import WbMethod
from ...types import ItemsItem, RequestLimit, SearchClustersStatisticsItem


class GetSearchClustersStatistics(WbMethod):
    """
    The method returns statistics for search clusters over a specified period. You can use this
    methodonly for campaigns with a `cpm` payment model — for displays.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v0~1normquery~1stats/post
    """

    __return__ = SearchClustersStatisticsItem
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/stats"
    __http_method__ = "POST"
    __data_key__ = "stats"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    from_: str = Field(alias="from")
    to: str = Field(alias="to")
    items: list[ItemsItem] = Field(alias="items")
