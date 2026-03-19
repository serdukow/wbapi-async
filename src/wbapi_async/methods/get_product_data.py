from pydantic import Field

from ..enums.product_data_availability import ProductDataAvailability
from ..enums.product_data_order_field import ProductDataOrderField
from ..enums.product_data_order_mode import ProductDataOrderMode
from ..enums.product_data_stock_type import ProductDataStockType
from ..types.base import BaseType
from ..types.product_data import ProductDataItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class Period(BaseType):
    start: str = Field(alias="start")
    end: str = Field(alias="end")


class OrderBy(BaseType):
    field: ProductDataOrderField = Field(alias="field")
    mode: ProductDataOrderMode = Field(alias="mode")


class GetProductData(WbMethod):
    """
    Forms a dataset for inventory by products.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post
    """

    __return__ = ProductDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/products"
    __http_method__ = "POST"
    __data_key__ = "data.items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20000, burst=3)

    current_period: Period = Field(alias="currentPeriod")
    stock_type: ProductDataStockType = Field(alias="stockType")
    skip_deleted_nm: bool = Field(alias="skipDeletedNm")
    order_by: OrderBy = Field(alias="orderBy")
    availability_filters: list[ProductDataAvailability] = Field(alias="availabilityFilters")
    limit: int = Field(100, alias="limit")
    offset: int = Field(0, alias="offset")

    nm_ids: list[int] | None = Field(None, alias="nmIDs")
    subject_id: int | None = Field(None, alias="subjectID")
    brand_name: str | None = Field(None, alias="brandName")
    tag_id: int | None = Field(None, alias="tagID")
