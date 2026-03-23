from pydantic import Field

from ...methods.base import WbMethod
from ...types import AssemblyOrdersItem, RequestLimit


class GetAssemblyOrders(WbMethod):
    """
    Returns assembly orders information without current status. You can get data for a specified
    period,maximum of 30 calendar days per request.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get
    """

    __return__ = AssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders"
    __data_key__ = "orders"
    __pagination__ = "next"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int = Field()
    next_: int = Field(alias="next")
    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
