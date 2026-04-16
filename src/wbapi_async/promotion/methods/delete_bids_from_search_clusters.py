from pydantic import Field

from ...methods.base import WbMethod
from ...types import DeleteBidsFromSearchClustersResponse, RequestLimit, V0SetNormQueryBidsRequestItem


class DeleteBidsFromSearchClusters(WbMethod):
    """
    The method deletes the bids from search clusters. You can use this method only for campaigns
    with:- custom bid - a `cpm` payment model — per displays

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1bids/delete
    """

    __return__ = DeleteBidsFromSearchClustersResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/bids"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    bids: list[V0SetNormQueryBidsRequestItem] = Field()
