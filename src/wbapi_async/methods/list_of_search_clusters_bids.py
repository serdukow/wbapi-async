from typing import Any

from pydantic import Field

from ..types.list_of_search_clusters_bids_item import ListOfSearchClustersBidsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ListOfSearchClustersBids(WbMethod):
    """
    The method returns a list of search clusters with bids by:

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1get-bids/post
    """

    __return__ = ListOfSearchClustersBidsItem
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/get-bids"
    __http_method__ = "POST"
    __data_key__ = "bids"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=10)

    items: list[Any] = Field(None)
