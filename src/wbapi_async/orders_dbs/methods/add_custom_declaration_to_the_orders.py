from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddCustomDeclarationToTheOrdersResponse, OrdersItem, RequestLimit


class AddCustomDeclarationToTheOrders(WbMethod):
    """
    Sets the cargo customs declaration number in the metadata of the assembly orders.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1customs-declaration/post
    """

    __return__ = AddCustomDeclarationToTheOrdersResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/customs-declaration"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[OrdersItem] | None = Field(None, alias="orders")
