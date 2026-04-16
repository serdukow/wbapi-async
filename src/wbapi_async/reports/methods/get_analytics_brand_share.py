from pydantic import Field

from ...methods.base import WbMethod
from ...types import AnalyticsBrandShareItem, RequestLimit


class GetAnalyticsBrandShare(WbMethod):
    """
    Returns a report on the brand's share in sales.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Share-of-Brand-in-Sales/paths/~1api~1v1~1analytics~1brand-share/get
    """

    __return__ = AnalyticsBrandShareItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/brand-share"
    __data_key__ = "report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    parent_id: int = Field(alias="parentId")
    brand: str = Field(alias="brand")
    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
