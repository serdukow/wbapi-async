from pydantic import Field

from ..types.orders_response import OrdersResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetOrders(WbMethod):
    """
    The method returns order information.<br>The data updated every 30 minutes.<br><br>

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1orders/get
    """

    __return__ = OrdersResponse
    __api__ = "statistics-api"
    __method__ = "api/v1/supplier/orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=1, burst=1)

    date_from: str = Field(None, alias="dateFrom")
    flag: int | None = Field(0)
