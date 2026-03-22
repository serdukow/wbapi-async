from pydantic import Field

from ..types.assembly_orders_item import AssemblyOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetAssemblyOrders(WbMethod):
    """
    Returns assembly orders information without current status. <br>You can get data for a
    specifiedperiod, maximum of 30 calendar days per request.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get
    """

    __return__ = AssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    limit: int = Field(None)
    next: int = Field(None)
    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
