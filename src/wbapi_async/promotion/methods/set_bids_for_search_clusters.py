from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SetBidsForSearchClustersResponse


class SetBidsForSearchClusters(WbMethod):
    """
    The method sets the bids for search clusters. You can use this method only for campaigns with:
    -custom bid - a `cpm` payment model — per displays

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1bids/post
    """

    __return__ = SetBidsForSearchClustersResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/bids"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    bids: list[Any] = Field()
