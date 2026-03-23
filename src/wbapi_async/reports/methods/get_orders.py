from pydantic import Field

from ...types import OrdersResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetOrders(WbMethod):
    """
    The method returns order information. The data updated every 30 minutes.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1orders/get
    """

    __return__ = OrdersResponse
    __api__ = "statistics-api"
    __method__ = "api/v1/supplier/orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    flag: int | None = Field(0)
