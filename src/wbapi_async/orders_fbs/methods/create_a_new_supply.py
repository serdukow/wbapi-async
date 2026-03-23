from pydantic import Field

from ...types import CreateANewSupplyResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class CreateANewSupply(WbMethod):
    """
    **Supplies limitations**:

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies/post
    """

    __return__ = CreateANewSupplyResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/supplies"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    name: str | None = Field(None)
