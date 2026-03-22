from pydantic import Field

from ...methods.base import WbMethod
from ...types import ReceivingCostsHistoryResponse, RequestLimit


class GetReceivingCostsHistory(WbMethod):
    """
    The method allows to get a costs history

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1upd/get
    """

    __return__ = ReceivingCostsHistoryResponse
    __api__ = "advert-api"
    __method__ = "adv/v1/upd"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    from_: str = Field(alias="from")
    to: str = Field()
