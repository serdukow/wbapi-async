from typing import Any

from pydantic import Field

from ...types import CreateProductCardsWithMergeResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class CreateProductCardsWithMerge(WbMethod):
    """
    The method creates product cards by merging it with existing individual cards and groups of
    mergedcards. There can be no more than 30 cards in one group of merged product cards,
    respectively,you can create no more than 29 product cards in one request. The dimensions of the
    productscan only be specified in `centimeters`, and the weight of packed products must be
    specifiedin `kilograms`. If this method response is Success (`200`) but product card was not
    updated,check errors using [list of failed nomenclature with
    errors](/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1error~1list/post).
    Productcards are created asynchronously. The process of synchronizing a new card with services
    maytake up to 30 minutes. During this time, you can't add inventory to warehouses and set
    prices.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload~1add/post
    """

    __return__ = CreateProductCardsWithMergeResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/upload/add"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    imt_id: int | None = Field(None, alias="imtID")
    cards_to_add: list[dict[str, Any]] | None = Field(None, alias="cardsToAdd")
