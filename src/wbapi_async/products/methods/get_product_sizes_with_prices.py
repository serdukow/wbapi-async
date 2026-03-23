from pydantic import Field

from ...types import ProductSizesWithPricesItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetProductSizesWithPrices(WbMethod):
    """
    Returns sizes data for the product. Only for products from categories where size price setting
    isavailable. For these products `"editableSizePrice":true`.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1size~1nm/get
    """

    __return__ = ProductSizesWithPricesItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/list/goods/size/nm"
    __data_key__ = "data.listGoods"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int = Field()
    offset: int | None = Field(None)
    nm_id: int = Field(alias="nmID")
