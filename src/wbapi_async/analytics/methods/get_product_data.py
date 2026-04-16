from pydantic import Field

from ...methods.base import WbMethod
from ...types import OrderBy, ProductDataItem, RequestLimit, SelectedPeriod
from ..enums.availability_filters_item import AvailabilityFiltersItem
from ..enums.stock_type import StockType


class GetProductData(WbMethod):
    """
    Forms a dataset for inventory by products. You can get data for individual products as well as
    forthe entire report if there are no filters in the query: `nmIDs`, `subjectID`, `brandName`,
    `tagID`.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post
    """

    __return__ = ProductDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/products"
    __http_method__ = "POST"
    __data_key__ = "data.items"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nm_i_ds: list[int] | None = Field(None, alias="nmIDs")
    subject_id: int | None = Field(None, alias="subjectID")
    brand_name: str | None = Field(None, alias="brandName")
    tag_id: int | None = Field(None, alias="tagID")
    current_period: SelectedPeriod = Field(alias="currentPeriod")
    stock_type: StockType = Field(alias="stockType")
    skip_deleted_nm: bool = Field(alias="skipDeletedNm")
    order_by: OrderBy = Field(alias="orderBy")
    availability_filters: list[AvailabilityFiltersItem] = Field(alias="availabilityFilters")
    limit: int | None = Field(100)
    offset: int = Field()
