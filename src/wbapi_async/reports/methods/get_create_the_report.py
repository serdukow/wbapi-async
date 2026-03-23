from pydantic import Field

from ...types import CreateTheReportResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetCreateTheReport(WbMethod):
    """
    Creates a task for report generation. The parameters `groupBy` and `filter` can be set in any
    combination— similar to the
    [version](https://seller.wildberries.ru/analytics-reports/warehouse-remains)in the personal
    account.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Warehouses-Inventory-Report/paths/~1api~1v1~1warehouse_remains/get
    """

    __return__ = CreateTheReportResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/warehouse_remains"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field("ru")
    group_by_brand: bool | None = Field(False, alias="groupByBrand")
    group_by_subject: bool | None = Field(False, alias="groupBySubject")
    group_by_sa: bool | None = Field(False, alias="groupBySa")
    group_by_nm: bool | None = Field(False, alias="groupByNm")
    group_by_barcode: bool | None = Field(False, alias="groupByBarcode")
    group_by_size: bool | None = Field(False, alias="groupBySize")
    filter_pics: int | None = Field(0, alias="filterPics")
    filter_volume: int | None = Field(0, alias="filterVolume")
