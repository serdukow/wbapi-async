from pydantic import Field

from ..types.get_product_sizes_with_prices_item import GetProductSizesWithPricesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetProductSizesWithPrices(WbMethod):
    """
    Get Product Sizes with Prices

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1size~1nm/get
    """

    __return__ = GetProductSizesWithPricesItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/list/goods/size/nm"
    __data_key__ = "data.listGoods"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    limit: int = Field(None)
    offset: int | None = Field(None)
    nm_id: int = Field(None, alias="nmID")
