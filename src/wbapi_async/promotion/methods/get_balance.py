from ...methods.base import WbMethod
from ...types import BalanceItem, RequestLimit


class GetBalance(WbMethod):
    """
    The method allows to get information about the seller's net, balance and bonuses

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1balance/get
    """

    __return__ = BalanceItem
    __api__ = "advert-api"
    __method__ = "adv/v1/balance"
    __data_key__ = "cashbacks"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
