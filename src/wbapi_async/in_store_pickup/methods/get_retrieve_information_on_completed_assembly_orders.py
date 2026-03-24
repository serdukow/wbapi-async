from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, RetrieveInformationOnCompletedAssemblyOrdersItem


class GetRetrieveInformationOnCompletedAssemblyOrders(WbMethod):
    """
    The method provides information on completed assembly orders after the sale or cancellation of
    anorder.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders/get
    """

    __return__ = RetrieveInformationOnCompletedAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/click-collect/orders"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int = Field()
    next_: int = Field(alias="next")
    date_from: int = Field(alias="dateFrom")
    date_to: int = Field(alias="dateTo")
