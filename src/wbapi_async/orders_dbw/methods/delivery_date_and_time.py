from pydantic import Field

from ...types import DeliveryDateAndTimeItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class DeliveryDateAndTime(WbMethod):
    """
    Method provides information about the delivery date and time selected by the buyer for orders.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1delivery-date/post
    """

    __return__ = DeliveryDateAndTimeItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbw/orders/delivery-date"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] | None = Field(None)
