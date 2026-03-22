from typing import Any

from pydantic import Field

from ..types.product_cards_statistics_per_days_response import ProductCardsStatisticsPerDaysResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ProductCardsStatisticsPerDays(WbMethod):
    """
    The method returns statistics for product cards by day or by week.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1products~1history/post
    """

    __return__ = ProductCardsStatisticsPerDaysResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v3/sales-funnel/products/history"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    selected_period: Any = Field(None, alias="selectedPeriod")
    nm_ids: list[int] = Field(None, alias="nmIds")
    skip_deleted_nm: bool | None = Field(None, alias="skipDeletedNm")
    aggregation_level: str | None = Field("day", alias="aggregationLevel")
