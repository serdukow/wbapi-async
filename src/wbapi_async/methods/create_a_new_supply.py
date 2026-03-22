from pydantic import Field

from ..types.create_a_new_supply_response import CreateANewSupplyResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreateANewSupply(WbMethod):
    """
    **Supplies limitations**:

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies/post
    """

    __return__ = CreateANewSupplyResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/supplies"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    name: str | None = Field(None)
