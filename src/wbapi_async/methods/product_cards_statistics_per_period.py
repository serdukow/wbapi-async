from typing import Any

from pydantic import Field

from ..types.product_cards_statistics_per_period_response import ProductCardsStatisticsPerPeriodResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ProductCardsStatisticsPerPeriod(WbMethod):
    """
    The method generates a report on products by comparing key metrics for the current period with
    asimilar past one.<br><br>

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1products/post
    """

    __return__ = ProductCardsStatisticsPerPeriodResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v3/sales-funnel/products"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    selected_period: Any = Field(None, alias="selectedPeriod")
    past_period: Any | None = Field(None, alias="pastPeriod")
    nm_ids: list[int] | None = Field(None, alias="nmIds")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    subject_ids: list[int] | None = Field(None, alias="subjectIds")
    tag_ids: list[int] | None = Field(None, alias="tagIds")
    skip_deleted_nm: bool | None = Field(None, alias="skipDeletedNm")
    order_by: dict[str, Any] | None = Field(None, alias="orderBy")
    limit: int | None = Field(50)
    offset: int | None = Field(0)
