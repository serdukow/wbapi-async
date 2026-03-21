from typing import Any

from pydantic import Field

from ..types.product_cards_list_item import ProductCardsListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ProductCardsList(WbMethod):
    """
    <div class="description_auth">

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post
    """

    __return__ = ProductCardsListItem
    __api__ = "content-api"
    __method__ = "content/v2/get/cards/list"
    __http_method__ = "POST"
    __data_key__ = "cards"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    locale: str | None = Field(None)
    settings: dict[str, Any] | None = Field(None)
