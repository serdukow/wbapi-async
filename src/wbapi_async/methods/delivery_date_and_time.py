from pydantic import Field

from ..types.delivery_date_and_time_item import DeliveryDateAndTimeItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeliveryDateAndTime(WbMethod):
    """
    Method provides information about the delivery date and time selected by the buyer for orders.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders~1delivery-date/post
    """

    __return__ = DeliveryDateAndTimeItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbs/orders/delivery-date"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    orders: list[int] | None = Field(None)
