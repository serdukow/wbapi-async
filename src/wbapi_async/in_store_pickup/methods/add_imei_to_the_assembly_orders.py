from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddImeiToTheAssemblyOrdersItem, ApiImei, RequestLimit


class AddImeiToTheAssemblyOrders(WbMethod):
    """
    Sets the IMEI for the [assembly orders
    metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).
    Theassembly order can have only one IMEI. You can add the IMEI only for assembly orders in the
    `confirm`
    [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
    thatare delivered by Wildberries.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1imei/post
    """

    __return__ = AddImeiToTheAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/meta/imei"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[ApiImei] = Field()
