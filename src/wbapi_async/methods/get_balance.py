from ..types.balance_item import BalanceItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetBalance(WbMethod):
    """
    The method allows to get information about the seller's net, balance and bonuses<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1balance/get
    """

    __return__ = BalanceItem
    __api__ = "advert-api"
    __method__ = "adv/v1/balance"
    __data_key__ = "cashbacks"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=5)
