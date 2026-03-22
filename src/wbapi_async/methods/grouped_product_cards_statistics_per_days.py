from typing import Any

from pydantic import Field

from ..types.grouped_product_cards_statistics_per_days_item import GroupedProductCardsStatisticsPerDaysItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GroupedProductCardsStatisticsPerDays(WbMethod):
    """
    The method returns statistics for product cards by day or by week.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1grouped~1history/post
    """

    __return__ = GroupedProductCardsStatisticsPerDaysItem
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v3/sales-funnel/grouped/history"
    __http_method__ = "POST"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    selected_period: Any = Field(None, alias="selectedPeriod")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    subject_ids: list[int] | None = Field(None, alias="subjectIds")
    tag_ids: list[int] | None = Field(None, alias="tagIds")
    skip_deleted_nm: bool | None = Field(None, alias="skipDeletedNm")
    aggregation_level: str | None = Field("day", alias="aggregationLevel")
