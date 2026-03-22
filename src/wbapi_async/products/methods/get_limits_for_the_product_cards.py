from ...methods.base import WbMethod
from ...types import LimitsForTheProductCardsResponse, RequestLimit


class GetLimitsForTheProductCards(WbMethod):
    """
    The method allows to get separately free and paid vendor limits for creating product cards. To
    calculatethe number of cards that can be created, use the formula: (freeLimits + paidLimits) -
    Numberof cards created. All cards that can be obtained using the [product cards
    list](/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post)
    and[list of product cards that are in the
    trash](/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1trash/post)
    methodsare considered created.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1limits/get
    """

    __return__ = LimitsForTheProductCardsResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/limits"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
