from pydantic import Field

from ...methods.base import WbMethod
from ...types import ReceivingTheHistoryOfAccountTopupsResponse, RequestLimit


class GetReceivingTheHistoryOfAccountTopups(WbMethod):
    """
    The method allows you to get a history of top-ups.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1payments/get
    """

    __return__ = ReceivingTheHistoryOfAccountTopupsResponse
    __api__ = "advert-api"
    __method__ = "adv/v1/payments"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    from_: str | None = Field(None, alias="from")
    to: str | None = Field(None, alias="to")
