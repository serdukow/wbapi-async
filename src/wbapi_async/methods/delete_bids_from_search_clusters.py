from typing import Any

from pydantic import Field

from ..types.delete_bids_from_search_clusters_response import DeleteBidsFromSearchClustersResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteBidsFromSearchClusters(WbMethod):
    """
    The method deletes the bids from search clusters.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1bids/delete
    """

    __return__ = DeleteBidsFromSearchClustersResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/bids"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=10)

    bids: list[Any] = Field(None)
