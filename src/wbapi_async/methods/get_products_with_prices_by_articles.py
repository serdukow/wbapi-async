from pydantic import Field

from ..types.products_with_prices_by_articles_item import ProductsWithPricesByArticlesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetProductsWithPricesByArticles(WbMethod):
    """
    Returns product data by its article.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/post
    """

    __return__ = ProductsWithPricesByArticlesItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/list/goods/filter"
    __http_method__ = "POST"
    __data_key__ = "data.listGoods"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    nm_list: list[int] = Field(None, alias="nmList")
