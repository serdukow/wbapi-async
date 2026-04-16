from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import PaginationByGroupsResponse, RequestLimit


class GetPaginationByGroups(WbMethod):
    """
    Pagination by groups in the report. It is possible only if there is a filter by brand, subject,
    ortag.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1table~1groups/post
    """

    __return__ = PaginationByGroupsResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/search-report/table/groups"
    __http_method__ = "POST"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    current_period: dict[str, Any] = Field(alias="currentPeriod")
    past_period: dict[str, Any] | None = Field(None, alias="pastPeriod")
    nm_ids: list[int] | None = Field(None, alias="nmIds")
    subject_ids: list[int] | None = Field(None, alias="subjectIds")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    tag_ids: list[int] | None = Field(None, alias="tagIds")
    order_by: dict[str, Any] = Field(alias="orderBy")
    position_cluster: str = Field(alias="positionCluster")
    include_substituted_skus: bool | None = Field(True, alias="includeSubstitutedSKUs")
    include_search_texts: bool | None = Field(True, alias="includeSearchTexts")
    limit: int = Field(alias="limit")
    offset: int = Field(alias="offset")
