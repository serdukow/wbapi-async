from pydantic import Field

from ...methods.base import WbMethod
from ...types import InformationOnCompletedOrdersItem, RequestLimit


class GetInformationOnCompletedOrders(WbMethod):
    """
    Returns information on completed orders (either canceled or sold). You can get data for a
    specifiedperiod, maximum of 30 calendar days per request.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders/get
    """

    __return__ = InformationOnCompletedOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbw/orders"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int = Field()
    next_: int = Field(alias="next")
    date_from: int = Field(alias="dateFrom")
    date_to: int = Field(alias="dateTo")
