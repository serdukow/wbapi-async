from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem, RequestLimit


class AddUinUniqueIdentificationNumbersToTheAssemblyOrders(WbMethod):
    """
    The method sets the UIN (Unique Identification Numbers) for the [assembly orders
    metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).
    Theorder can only have one UIN. You can add the UIN only for assembly orders in the `confirm`
    [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
    andthat are delivered by WB.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1uin/post
    """

    __return__ = AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/meta/uin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[Any] = Field()
