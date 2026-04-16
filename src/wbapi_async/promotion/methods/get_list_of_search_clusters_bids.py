from pydantic import Field

from ...methods.base import WbMethod
from ...types import ListOfSearchClustersBidsItem, RequestLimit, V0GetNormQueryBidsRequestItem


class GetListOfSearchClustersBids(WbMethod):
    """
    The method returns a list of search clusters with bids by: - campaign IDs - WB articles

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1get-bids/post
    """

    __return__ = ListOfSearchClustersBidsItem
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/get-bids"
    __http_method__ = "POST"
    __data_key__ = "bids"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    items: list[V0GetNormQueryBidsRequestItem] = Field(alias="items")
