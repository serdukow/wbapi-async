from pydantic import Field

from ..types.receiving_the_history_of_account_topups_response import ReceivingTheHistoryOfAccountTopupsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetReceivingTheHistoryOfAccountTopups(WbMethod):
    """
    The method allows you to get a history of top-ups.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1payments/get
    """

    __return__ = ReceivingTheHistoryOfAccountTopupsResponse
    __api__ = "advert-api"
    __method__ = "adv/v1/payments"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=5)

    from_: str | None = Field(None, alias="from")
    to: str | None = Field(None)
