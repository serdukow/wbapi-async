from pydantic import Field

from ...methods.base import WbMethod
from ...types import OrderBy, ProductCardsStatisticsPerPeriodItem, RequestLimit, SelectedPeriod


class GetProductCardsStatisticsPerPeriod(WbMethod):
    """
    The method generates a report on products by comparing key metrics for the current period with
    asimilar past one.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1products/post
    """

    __return__ = ProductCardsStatisticsPerPeriodItem
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v3/sales-funnel/products"
    __http_method__ = "POST"
    __data_key__ = "data.products"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    selected_period: SelectedPeriod = Field(alias="selectedPeriod")
    past_period: SelectedPeriod | None = Field(None, alias="pastPeriod")
    nm_ids: list[int] | None = Field(None, alias="nmIds")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    subject_ids: list[int] | None = Field(None, alias="subjectIds")
    tag_ids: list[int] | None = Field(None, alias="tagIds")
    skip_deleted_nm: bool | None = Field(None, alias="skipDeletedNm")
    order_by: OrderBy | None = Field(None, alias="orderBy")
    limit: int | None = Field(50, alias="limit")
    offset: int | None = Field(0, alias="offset")
