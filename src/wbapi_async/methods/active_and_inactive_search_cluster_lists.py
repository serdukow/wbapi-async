from typing import Any

from pydantic import Field

from ..types.active_and_inactive_search_cluster_lists_item import ActiveAndInactiveSearchClusterListsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ActiveAndInactiveSearchClusterLists(WbMethod):
    """
    Returns lists of active and inactive search clusters with at least 100 views.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1list/post
    """

    __return__ = ActiveAndInactiveSearchClusterListsItem
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/list"
    __http_method__ = "POST"
    __data_key__ = "items"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=10)

    items: list[Any] = Field(None)
