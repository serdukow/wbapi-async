from pydantic import Field

from ..types.retrieve_information_on_completed_assembly_orders_item import RetrieveInformationOnCompletedAssemblyOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    limit: int = Field(None)
    next: int = Field(None)
    date_from: int = Field(None, alias="dateFrom")
    date_to: int = Field(None, alias="dateTo")
