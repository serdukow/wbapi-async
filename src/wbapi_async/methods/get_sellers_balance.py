from ..types.sellers_balance_response import SellersBalanceResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSellersBalance(WbMethod):
    """
    Balance widget data on [the main page](https://seller.wildberries.ru) of the sellers portal.

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Balance/paths/~1api~1v1~1account~1balance/get
    """

    __return__ = SellersBalanceResponse
    __api__ = "finance-api"
    __method__ = "api/v1/account/balance"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=1)
