from typing import Any

from pydantic import Field

from ..types.search_texts_by_product_response import SearchTextsByProductResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class SearchTextsByProduct(WbMethod):
    """
    Forms the top search texts by product.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1product~1search-texts/post
    """

    __return__ = SearchTextsByProductResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/search-report/product/search-texts"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    current_period: dict[str, Any] = Field(None, alias="currentPeriod")
    past_period: dict[str, Any] | None = Field(None, alias="pastPeriod")
    nm_ids: list[int] = Field(None, alias="nmIds")
    top_order_by: str = Field(None, alias="topOrderBy")
    include_substituted_sk_us: bool | None = Field(True, alias="includeSubstitutedSKUs")
    include_search_texts: bool | None = Field(True, alias="includeSearchTexts")
    order_by: dict[str, Any] = Field(None, alias="orderBy")
    limit: Any = Field(None)
