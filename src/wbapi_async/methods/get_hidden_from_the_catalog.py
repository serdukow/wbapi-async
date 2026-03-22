from pydantic import Field

from ..types.hidden_from_the_catalog_item import HiddenFromTheCatalogItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=10, limit=1, interval=10, burst=6)

    sort: str = Field(None)
    order: str = Field(None)
