from pydantic import Field

from ...communications.enums.order import Order
from ...methods.base import WbMethod
from ...types import Cursor, ListOfFailedProductCardsWithErrorsItem, RequestLimit


class GetListOfFailedProductCardsWithErrors(WbMethod):
    """
    Returns the list of product cards
    ([drafts](https://seller.wildberries.ru/new-goods/error-cards))and the list of errors
    encounteredduring product card creation or editing. The data is returned in batches. One batch
    contains:- all errors for one `variants` array in one request during product cards
    [creation](/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload/post)
    -all errors in one request during product cards [creation with
    merge](/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload~1add/post)
    or
    [editing](/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1update/post).
    Toget more than 100 batches, use pagination:

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1error~1list/post
    """

    __return__ = ListOfFailedProductCardsWithErrorsItem
    __api__ = "content-api"
    __method__ = "content/v2/cards/error/list"
    __http_method__ = "POST"
    __data_key__ = "data.items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field(None)
    cursor: Cursor | None = Field(None)
    order: Order | None = Field(None)
