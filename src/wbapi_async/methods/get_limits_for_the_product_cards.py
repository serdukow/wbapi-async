from ..types.limits_for_the_product_cards_response import LimitsForTheProductCardsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetLimitsForTheProductCards(WbMethod):
    """
    The method allows to get separately free and paid vendor limits for creating product cards.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1limits/get
    """

    __return__ = LimitsForTheProductCardsResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/limits"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)
