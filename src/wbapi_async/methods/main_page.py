from typing import Any

from pydantic import Field

from ..types.main_page_response import MainPageResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class MainPage(WbMethod):
    """
    Forms a dataset for the main report page with:

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1report/post
    """

    __return__ = MainPageResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/search-report/report"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    current_period: dict[str, Any] = Field(None, alias="currentPeriod")
    past_period: dict[str, Any] | None = Field(None, alias="pastPeriod")
    nm_ids: list[int] | None = Field(None, alias="nmIds")
    subject_ids: list[int] | None = Field(None, alias="subjectIds")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    tag_ids: list[int] | None = Field(None, alias="tagIds")
    position_cluster: str = Field(None, alias="positionCluster")
    order_by: dict[str, Any] = Field(None, alias="orderBy")
    include_substituted_sk_us: bool | None = Field(True, alias="includeSubstitutedSKUs")
    include_search_texts: bool | None = Field(True, alias="includeSearchTexts")
    limit: int = Field(None)
    offset: int = Field(None)
