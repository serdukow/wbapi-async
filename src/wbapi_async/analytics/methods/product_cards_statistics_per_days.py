from typing import Any

from pydantic import Field

from ...enums import AggregationLevel
from ...methods.base import WbMethod
from ...types import ProductCardsStatisticsPerDaysResponse, RequestLimit


class ProductCardsStatisticsPerDays(WbMethod):
    """
    The method returns statistics for product cards by day or by week. You can get data for a
    maximumof the last week.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1products~1history/post
    """

    __return__ = ProductCardsStatisticsPerDaysResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v3/sales-funnel/products/history"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    selected_period: Any = Field(alias="selectedPeriod")
    nm_ids: list[int] = Field(alias="nmIds")
    skip_deleted_nm: bool | None = Field(None, alias="skipDeletedNm")
    aggregation_level: AggregationLevel | None = Field("day", alias="aggregationLevel")
