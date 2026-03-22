from typing import Any

from pydantic import Field

from ..types.pagination_by_products_within_a_group_response import PaginationByProductsWithinAGroupResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class PaginationByProductsWithinAGroup(WbMethod):
    """
    Pagination by products within a group. It is possible regardless of the presence of filters.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1table~1details/post
    """

    __return__ = PaginationByProductsWithinAGroupResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/search-report/table/details"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    current_period: dict[str, Any] = Field(None, alias="currentPeriod")
    past_period: dict[str, Any] | None = Field(None, alias="pastPeriod")
    subject_id: int | None = Field(None, alias="subjectId")
    brand_name: str | None = Field(None, alias="brandName")
    tag_id: int | None = Field(None, alias="tagId")
    nm_ids: list[int] | None = Field(None, alias="nmIds")
    order_by: dict[str, Any] = Field(None, alias="orderBy")
    position_cluster: str = Field(None, alias="positionCluster")
    include_substituted_sk_us: bool | None = Field(True, alias="includeSubstitutedSKUs")
    include_search_texts: bool | None = Field(True, alias="includeSearchTexts")
    limit: int = Field(None)
    offset: int = Field(None)
