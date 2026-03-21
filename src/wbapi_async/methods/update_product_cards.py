from ..types.request_limit import RequestLimit
from ..types.update_product_cards_response import UpdateProductCardsResponse
from .base import WbMethod


class UpdateProductCards(WbMethod):
    """
    Update Product Cards

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1update/post
    """

    __return__ = UpdateProductCardsResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/update"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=6, burst=5)
