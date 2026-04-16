from pydantic import Field

from ...methods.base import WbMethod
from ...types import MainPageResponse, OrderBy, RequestLimit, SelectedPeriod


class GetMainPage(WbMethod):
    """
    Forms a dataset for the main report page with: - General information - Product positions - Data
    onvisibility and transitions to the product card - Data for the table by groups

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1report/post
    """

    __return__ = MainPageResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/search-report/report"
    __http_method__ = "POST"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    current_period: SelectedPeriod = Field(alias="currentPeriod")
    past_period: SelectedPeriod | None = Field(None, alias="pastPeriod")
    nm_ids: list[int] | None = Field(None, alias="nmIds")
    subject_ids: list[int] | None = Field(None, alias="subjectIds")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    tag_ids: list[int] | None = Field(None, alias="tagIds")
    position_cluster: str = Field(alias="positionCluster")
    order_by: OrderBy = Field(alias="orderBy")
    include_substituted_skus: bool | None = Field(True, alias="includeSubstitutedSKUs")
    include_search_texts: bool | None = Field(True, alias="includeSearchTexts")
    limit: int = Field(alias="limit")
    offset: int = Field(alias="offset")
