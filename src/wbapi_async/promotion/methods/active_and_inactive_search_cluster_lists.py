from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import ActiveAndInactiveSearchClusterListsItem, RequestLimit


class ActiveAndInactiveSearchClusterLists(WbMethod):
    """
    Returns lists of active and inactive search clusters with at least 100 views. Request limit per
    oneseller's account:

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1list/post
    """

    __return__ = ActiveAndInactiveSearchClusterListsItem
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/list"
    __http_method__ = "POST"
    __data_key__ = "items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    items: list[Any] = Field()
