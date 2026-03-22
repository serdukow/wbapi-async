from ...methods.base import WbMethod
from ...types import CreateProductCardsResponse, RequestLimit


class CreateProductCards(WbMethod):
    """
    Creates products cards. You can specify product description and characteristics.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload/post
    """

    __return__ = CreateProductCardsResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/upload"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
