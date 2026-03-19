from pydantic import Field

from ..types.product_with_price import ProductWithPrice
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetProductsWithPrices(WbMethod):
    __return__ = ProductWithPrice
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/list/goods/filter"
    __data_key__ = "data.listGoods"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    limit: int = 1000
    offset: int = 0
    filter_nm_id: int | None = Field(None, alias="filterNmID")
