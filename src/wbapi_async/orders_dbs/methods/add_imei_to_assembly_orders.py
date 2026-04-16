from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddImeiToAssemblyOrdersItem, ApiImei, RequestLimit


class AddImeiToAssemblyOrders(WbMethod):
    """
    Sets the IMEI for the [assembly orders
    metadata](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).
    Theassembly order can have only one IMEI. You can add the IMEI only for orders in the
    `confirmed`
    [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
    andthat are delivered by Wildberries.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1imei/post
    """

    __return__ = AddImeiToAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/imei"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[ApiImei] = Field(alias="orders")
