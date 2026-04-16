from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddGtinToAssemblyOrdersItem, ApiGtin, RequestLimit


class AddGtinToAssemblyOrders(WbMethod):
    """
    Sets the GTIN, Belarus product unique identifier, for the assembly order
    metadata(./orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).
    Theassembly order can only have one GTIN. You can set the GTIN only for orders in the
    `confirmed`
    [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
    andthat are delivered by Wildberries.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1gtin/post
    """

    __return__ = AddGtinToAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/gtin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[ApiGtin] = Field(alias="orders")
