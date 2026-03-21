from ..types.create_product_cards_response import CreateProductCardsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreateProductCards(WbMethod):
    """
    Create Product Cards

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload/post
    """

    __return__ = CreateProductCardsResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/upload"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=6, burst=5)
