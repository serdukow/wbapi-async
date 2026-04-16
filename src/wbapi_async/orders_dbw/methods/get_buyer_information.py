from pydantic import Field

from ...methods.base import WbMethod
from ...types import BuyerInformationItem, RequestLimit


class GetBuyerInformation(WbMethod):
    """
    The method returns buyers information by order IDs.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbw~1orders~1client/post
    """

    __return__ = BuyerInformationItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbw/orders/client"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] | None = Field(None, alias="orders")
