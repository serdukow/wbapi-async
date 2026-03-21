from pydantic import Field

from ..types.get_products_in_quarantine_item import GetProductsInQuarantineItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetProductsInQuarantine(WbMethod):
    """
    Get Products in Quarantine

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1quarantine~1goods/get
    """

    __return__ = GetProductsInQuarantineItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/quarantine/goods"
    __data_key__ = "data.quarantineGoods"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    limit: int = Field(None)
    offset: int | None = Field(None)
