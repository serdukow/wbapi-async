from pydantic import Field

from ...methods.base import WbMethod
from ...types import CourierInfoItem, RequestLimit


class CourierInfo(WbMethod):
    """
    Method provides the courier's contact information and vehicle number based on the assembly
    orderID. For assembly orders in the statuses `confirm` and `complete`.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1courier/post
    """

    __return__ = CourierInfoItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbw/orders/courier"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] | None = Field(None)
