from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProductDataItem, RequestLimit
from ..enums.product_data_availability import ProductDataAvailability
from ..enums.product_data_stock_type import ProductDataStockType
from ..types.product_data_order_by import ProductDataOrderBy
from ..types.product_data_period import ProductDataPeriod


class ProductData(WbMethod):
    """
    Forms a dataset for inventory by products. You can get data for individual products as well as
    for the entire report if there are no filters in the query: `nmIDs`, `subjectID`, `brandName`,
    `tagID`.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post
    """

    __return__ = ProductDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/products"
    __http_method__ = "POST"
    __data_key__ = "data.items"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    nm_ids: list[int] | None = Field(None, alias="nmIDs")
    subject_id: int | None = Field(None, alias="subjectID")
    brand_name: str | None = Field(None, alias="brandName")
    tag_id: int | None = Field(None, alias="tagID")
    current_period: ProductDataPeriod = Field(alias="currentPeriod")
    stock_type: ProductDataStockType = Field(alias="stockType")
    skip_deleted_nm: bool = Field(alias="skipDeletedNm")
    order_by: ProductDataOrderBy = Field(alias="orderBy")
    availability_filters: list[ProductDataAvailability] = Field(alias="availabilityFilters")
    limit: int | None = Field(1000)
    offset: int = Field(0)
