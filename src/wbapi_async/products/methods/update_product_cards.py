from ...methods.base import WbMethod
from ...types import RequestLimit, UpdateProductCardsResponse


class UpdateProductCards(WbMethod):
    """
    Edits product cards. Also use it to add new sizes.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1update/post
    """

    __return__ = UpdateProductCardsResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/update"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
