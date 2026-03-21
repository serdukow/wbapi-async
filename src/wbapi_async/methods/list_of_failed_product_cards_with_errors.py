from typing import Any

from pydantic import Field

from ..types.list_of_failed_product_cards_with_errors_item import (
    ListOfFailedProductCardsWithErrorsItem,
)
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ListOfFailedProductCardsWithErrors(WbMethod):
    """
    List of Failed Product Cards with Errors

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1error~1list/post
    """

    __return__ = ListOfFailedProductCardsWithErrorsItem
    __api__ = "content-api"
    __method__ = "content/v2/cards/error/list"
    __http_method__ = "POST"
    __data_key__ = "data.items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=6, burst=5)

    locale: str | None = Field(None)
    cursor: dict[str, Any] | None = Field(None)
    order: dict[str, Any] | None = Field(None)
