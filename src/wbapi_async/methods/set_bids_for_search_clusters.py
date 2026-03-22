from typing import Any

from pydantic import Field

from ..types.set_bids_for_search_clusters_response import SetBidsForSearchClustersResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class SetBidsForSearchClusters(WbMethod):
    """
    The method sets the bids for search clusters.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1bids/post
    """

    __return__ = SetBidsForSearchClustersResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/bids"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=1, limit=2, interval=500, burst=4)

    bids: list[Any] = Field(None)
