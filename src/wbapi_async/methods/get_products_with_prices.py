from pydantic import Field

from ..types.get_products_with_prices_item import GetProductsWithPricesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetProductsWithPrices(WbMethod):
    """
    Get Products with Prices

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/get
    """

    __return__ = GetProductsWithPricesItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/list/goods/filter"
    __data_key__ = "data.listGoods"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    limit: int = Field(None)
    offset: int | None = Field(None)
    filter_nm_id: int | None = Field(None, alias="filterNmID")
