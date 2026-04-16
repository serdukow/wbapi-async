from pydantic import Field

from ...methods.base import WbMethod
from ...types import InformationOnPaidDeliveryResponse, RequestLimit


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    groups: list[str] | None = Field(None, alias="groups")
