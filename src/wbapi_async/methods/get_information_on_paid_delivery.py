from pydantic import Field

from ..types.information_on_paid_delivery_response import InformationOnPaidDeliveryResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetInformationOnPaidDelivery(WbMethod):
    """
    The method provides information on paid delivery for assembly orders that have been received at
    asingle warehouse (warehouseId) as part of a single buyer transaction (orderUid).

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1groups~1info/post
    """

    __return__ = InformationOnPaidDeliveryResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbs/groups/info"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    groups: list[str] | None = Field(None)
