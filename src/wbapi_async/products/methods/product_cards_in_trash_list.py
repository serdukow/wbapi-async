from typing import Any

from pydantic import Field

from ...enums import Locale
from ...methods.base import WbMethod
from ...types import ProductCardsInTrashListItem, RequestLimit


class ProductCardsInTrashList(WbMethod):
    """
    The method is available with the token of the Promotion category

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1trash/post
    """

    __return__ = ProductCardsInTrashListItem
    __api__ = "content-api"
    __method__ = "content/v2/get/cards/trash"
    __http_method__ = "POST"
    __data_key__ = "cards"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: Locale | None = Field(None)
    settings: dict[str, Any] | None = Field(None)
