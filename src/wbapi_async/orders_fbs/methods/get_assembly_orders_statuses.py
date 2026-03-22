from pydantic import Field

from ...methods.base import WbMethod
from ...types import AssemblyOrdersStatusesItem, RequestLimit


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] = Field()
