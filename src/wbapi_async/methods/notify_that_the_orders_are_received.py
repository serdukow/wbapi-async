from typing import Any

from pydantic import Field

from ..types.notify_that_the_orders_are_received_item import NotifyThatTheOrdersAreReceivedItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class NotifyThatTheOrdersAreReceived(WbMethod):
    """
    The method transfers [assembly orders](/openapi/orders-dbs#tag/DBS-Assembly-Orders) with the
    `deliver`
    [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
    tothe `receive` status — received by the buyer.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1receive/post
    """

    __return__ = NotifyThatTheOrdersAreReceivedItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/status/receive"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=10)

    orders: list[Any] = Field(None)
