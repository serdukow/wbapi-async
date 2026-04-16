from pydantic import Field

from ...methods.base import WbMethod
from ...types import GroupDataItem, OrderBy, RequestLimit, SelectedPeriod


class GetGroupData(WbMethod):
    """
    Forms a dataset for inventory by product group. The product group is described by a tuple of
    `subjectID,brandName, tagID`.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1groups/post
    """

    __return__ = GroupDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/groups"
    __http_method__ = "POST"
    __data_key__ = "data.groups"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nm_ids: list[int] | None = Field(None, alias="nmIDs")
    subject_ids: list[int] | None = Field(None, alias="subjectIDs")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    tag_ids: list[int] | None = Field(None, alias="tagIDs")
    current_period: SelectedPeriod = Field(alias="currentPeriod")
    stock_type: str = Field(alias="stockType")
    skip_deleted_nm: bool = Field(alias="skipDeletedNm")
    availability_filters: list[str] = Field(alias="availabilityFilters")
    order_by: OrderBy = Field(alias="orderBy")
    limit: int | None = Field(100, alias="limit")
    offset: int = Field(alias="offset")
