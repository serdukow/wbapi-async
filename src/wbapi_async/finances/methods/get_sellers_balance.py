from ...types import RequestLimit
from ...types import SellersBalanceResponse
from ...methods.base import WbMethod


class GetSellersBalance(WbMethod):
    """
    Balance widget data on [the main page](https://seller.wildberries.ru) of the sellers portal.

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Balance/paths/~1api~1v1~1account~1balance/get
    """

    __return__ = SellersBalanceResponse
    __api__ = "finance-api"
    __method__ = "api/v1/account/balance"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
