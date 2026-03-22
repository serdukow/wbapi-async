from pydantic import Field

from ..types.receiving_costs_history_response import ReceivingCostsHistoryResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetReceivingCostsHistory(WbMethod):
    """
    The method allows to get a costs history

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1upd/get
    """

    __return__ = ReceivingCostsHistoryResponse
    __api__ = "advert-api"
    __method__ = "adv/v1/upd"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=5)

    from_: str = Field(None, alias="from")
    to: str = Field(None)
