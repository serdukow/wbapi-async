from pydantic import Field

from ...methods.base import WbMethod
from ...types import ApiOrderCodeRequest, NotifyThatTheOrdersAreDeclinedItem, RequestLimit


class NotifyThatTheOrdersAreDeclined(WbMethod):
    """
    The method transfers [assembly orders](/openapi/orders-dbs#tag/DBS-Assembly-Orders) with the
    `deliver`
    [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
    tothe `reject` status — declined upon receipt.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1reject/post
    """

    __return__ = NotifyThatTheOrdersAreDeclinedItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/status/reject"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[ApiOrderCodeRequest] = Field()
