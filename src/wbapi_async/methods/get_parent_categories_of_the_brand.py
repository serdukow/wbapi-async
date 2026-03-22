from pydantic import Field

from ..types.parent_categories_of_the_brand_item import ParentCategoriesOfTheBrandItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetParentCategoriesOfTheBrand(WbMethod):
    """
    Returns parent categories of the brand.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Share-of-Brand-in-Sales/paths/~1api~1v1~1analytics~1brand-share~1parent-subjects/get
    """

    __return__ = ParentCategoriesOfTheBrandItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/brand-share/parent-subjects"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=5, limit=1, interval=5, burst=20)

    locale: str | None = Field("ru")
    brand: str = Field(None)
    date_from: str = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
