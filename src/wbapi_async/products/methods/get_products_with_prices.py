from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProductsWithPricesItem, RequestLimit


class GetProductsWithPrices(WbMethod):
    """
    Returns product data. You can specify only one article in one request. To get data for all
    products,do not set the article, set `limit=1000`, and use the `offset` field to set the data
    offset.The offset should be calculated using the formula: `offset` plus `limit` from the
    previousrequest. Repeat the request until you receive a response with an empty array. Use
    separatemethods to get data: - for [more than one product by
    article](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/post)
    -for [the size of the
    product](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1size~1nm/get)

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/get
    """

    __return__ = ProductsWithPricesItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/list/goods/filter"
    __data_key__ = "data.listGoods"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int = Field()
    offset: int | None = Field(None)
    filter_nm_id: int | None = Field(None, alias="filterNmID")
