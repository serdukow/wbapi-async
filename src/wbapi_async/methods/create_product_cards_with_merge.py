from typing import Any

from pydantic import Field

from ..types.create_product_cards_with_merge_response import CreateProductCardsWithMergeResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreateProductCardsWithMerge(WbMethod):
    """
    The method creates product cards by merging it with existing individual cards and groups of
    mergedcards. There can be no more than 30 cards in one group of merged product cards,
    respectively,you can create no more than 29 product cards in one request.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload~1add/post
    """

    __return__ = CreateProductCardsWithMergeResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/upload/add"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=6, burst=5)

    imt_id: int | None = Field(None, alias="imtID")
    cards_to_add: list[dict[str, Any]] | None = Field(None, alias="cardsToAdd")
