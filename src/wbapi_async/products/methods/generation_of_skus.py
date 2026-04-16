from pydantic import Field

from ...methods.base import WbMethod
from ...types import GenerationOfSkusItem, RequestLimit


class GenerationOfSkus(WbMethod):
    """
    Generates array of unique SKUs to create size of the product card

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1barcodes/post
    """

    __return__ = GenerationOfSkusItem
    __api__ = "content-api"
    __method__ = "content/v2/barcodes"
    __http_method__ = "POST"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    count: int | None = Field(None, alias="count")
