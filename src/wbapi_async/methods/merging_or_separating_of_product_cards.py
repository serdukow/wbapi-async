from ..types.merging_or_separating_of_product_cards_response import MergingOrSeparatingOfProductCardsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class MergingOrSeparatingOfProductCards(WbMethod):
    """
    The method merges and separates product cards. Product cards are merged if they have the same
    `imtID`.<br><br>

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1moveNm/post
    """

    __return__ = MergingOrSeparatingOfProductCardsResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/moveNm"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)
