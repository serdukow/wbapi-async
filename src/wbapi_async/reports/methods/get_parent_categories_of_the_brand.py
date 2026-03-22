from pydantic import Field

from ...methods.base import WbMethod
from ...types import ParentCategoriesOfTheBrandItem, RequestLimit


class GetParentCategoriesOfTheBrand(WbMethod):
    """
    Returns parent categories of the brand.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Share-of-Brand-in-Sales/paths/~1api~1v1~1analytics~1brand-share~1parent-subjects/get
    """

    __return__ = ParentCategoriesOfTheBrandItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/brand-share/parent-subjects"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field("ru")
    brand: str = Field()
    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
