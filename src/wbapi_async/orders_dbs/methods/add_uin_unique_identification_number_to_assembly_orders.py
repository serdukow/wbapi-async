from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddUinUniqueIdentificationNumberToAssemblyOrdersItem, ApiUin, RequestLimit


class AddUinUniqueIdentificationNumberToAssemblyOrders(WbMethod):
    """
    Sets the UIN to the [assembly orders
    metadata](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).
    Theorder can only have one UIN. You can add the UIN only for assembly orders in the `confirmed`
    [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
    andthat are delivered by Wildberries.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1uin/post
    """

    __return__ = AddUinUniqueIdentificationNumberToAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/uin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[ApiUin] = Field(alias="orders")
