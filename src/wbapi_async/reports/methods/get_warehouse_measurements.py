from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, WarehouseMeasurementsItem


class GetWarehouseMeasurements(WbMethod):
    """
    The method returns a report with [warehouse
    measurements](https://seller.wildberries.ru/analytics-reports/dimensions-penalties/warehouse-measurements)

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1analytics~1v1~1warehouse-measurements/get
    """

    __return__ = WarehouseMeasurementsItem
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v1/warehouse-measurements"
    __data_key__ = "data.reports"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str | None = Field(None, alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int = Field()
    offset: int | None = Field(0)
