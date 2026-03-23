from pydantic import Field

from ...types import ProductsWithPricesByArticlesItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetProductsWithPricesByArticles(WbMethod):
    """
    Returns product data by its article. You can specify more than one article in one request. Use
    separatemethods to get data: - for [all products without specifying
    articles](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/get)
    -for [the size of the
    product](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1size~1nm/get).

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/post
    """

    __return__ = ProductsWithPricesByArticlesItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/list/goods/filter"
    __http_method__ = "POST"
    __data_key__ = "data.listGoods"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nm_list: list[int] = Field(alias="nmList")
