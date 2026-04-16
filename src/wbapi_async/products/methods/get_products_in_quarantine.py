from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProductsInQuarantineItem, RequestLimit


class GetProductsInQuarantine(WbMethod):
    """
    Returns information about products in quarantine. If the product new price with discount will
    beminimum 3 times less than the old price, the product will be placed in
    [quarantine](https://seller.wildberries.ru/discount-and-prices/quarantine)and will be sold at
    theold price. An error about this will be in the [upload
    states](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1tasks/get)
    methodresponse. You can change price or discount via API or release product from quarantine in
    [personalaccount](https://seller.wildberries.ru/discount-and-prices/quarantine). For products
    with[size-based
    pricing](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task~1size/post),
    quarantinedoes not apply.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1quarantine~1goods/get
    """

    __return__ = ProductsInQuarantineItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/quarantine/goods"
    __data_key__ = "data.quarantineGoods"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int = Field(alias="limit")
    offset: int | None = Field(None, alias="offset")
