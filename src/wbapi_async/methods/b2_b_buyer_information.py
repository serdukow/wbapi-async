from pydantic import Field

from ..types.b2_b_buyer_information_item import B2BBuyerInformationItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class B2BBuyerInformation(WbMethod):
    """
    The method returns B2B buyers data by assembly orders ID:

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1b2b~1info/post
    """

    __return__ = B2BBuyerInformationItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/b2b/info"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
