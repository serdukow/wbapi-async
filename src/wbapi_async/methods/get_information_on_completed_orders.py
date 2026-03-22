from pydantic import Field

from ..types.information_on_completed_orders_item import InformationOnCompletedOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetInformationOnCompletedOrders(WbMethod):
    """
    Returns information on completed orders (either canceled or sold). <br> You can get data for a
    specifiedperiod, maximum of 30 calendar days per request.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders/get
    """

    __return__ = InformationOnCompletedOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbs/orders"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    limit: int = Field(None)
    next: int = Field(None)
    date_from: int = Field(None, alias="dateFrom")
    date_to: int = Field(None, alias="dateTo")
