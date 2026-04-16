from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProductCardsListItem, RequestLimit


class GetProductCardsList(WbMethod):
    """
    The method is available with the token of the Promotion category

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post
    """

    __return__ = ProductCardsListItem
    __api__ = "content-api"
    __method__ = "content/v2/get/cards/list"
    __http_method__ = "POST"
    __data_key__ = "cards"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field(None, alias="locale")
    settings: dict[str, Any] | None = Field(None, alias="settings")
