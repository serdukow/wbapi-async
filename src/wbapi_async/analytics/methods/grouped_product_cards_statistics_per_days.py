from typing import Any

from pydantic import Field

from ...enums import AggregationLevel
from ...methods.base import WbMethod
from ...types import GroupedProductCardsStatisticsPerDaysItem, RequestLimit


class GroupedProductCardsStatisticsPerDays(WbMethod):
    """
    The method returns statistics for product cards by day or by week. Product cards are grouped by
    subjects,brands and tags. You can get data for a maximum of the last week.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1grouped~1history/post
    """

    __return__ = GroupedProductCardsStatisticsPerDaysItem
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v3/sales-funnel/grouped/history"
    __http_method__ = "POST"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    selected_period: Any = Field(alias="selectedPeriod")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    subject_ids: list[int] | None = Field(None, alias="subjectIds")
    tag_ids: list[int] | None = Field(None, alias="tagIds")
    skip_deleted_nm: bool | None = Field(None, alias="skipDeletedNm")
    aggregation_level: AggregationLevel | None = Field(AggregationLevel.DAY, alias="aggregationLevel")
