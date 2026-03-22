from pydantic import Field

from ..types.buyer_information_item import BuyerInformationItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class BuyerInformation(WbMethod):
    """
    The method provides information about the buyer based on the assembly order ID.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders~1client/post
    """

    __return__ = BuyerInformationItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/click-collect/orders/client"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    orders: list[int] | None = Field(None)
