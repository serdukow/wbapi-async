from pydantic import Field

from ..types.assembly_orders_statuses_item import AssemblyOrdersStatusesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetAssemblyOrdersStatuses(WbMethod):
    """
    Returns the statuses of assembly orders from the request.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1status/post
    """

    __return__ = AssemblyOrdersStatusesItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders/status"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    orders: list[int] = Field(None)
