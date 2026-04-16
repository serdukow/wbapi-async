from pydantic import Field

from ...analytics.enums.mode import Mode
from ...methods.base import WbMethod
from ...types import HiddenFromTheCatalogItem, RequestLimit
from ..enums.sort_shadowed import SortShadowed


class GetHiddenFromTheCatalog(WbMethod):
    """
    Returns the list of products [hidden from the
    catalog](https://seller.wildberries.ru/analytics-reports/banned-products/shadowed)

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Hidden-Products/paths/~1api~1v1~1analytics~1banned-products~1shadowed/get
    """

    __return__ = HiddenFromTheCatalogItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/banned-products/shadowed"
    __data_key__ = "report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    sort: SortShadowed = Field()
    order: Mode = Field()
