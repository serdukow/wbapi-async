from pydantic import Field

from ..types.logistics_and_storage_costs_multiplier_item import LogisticsAndStorageCostsMultiplierItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetLogisticsAndStorageCostsMultiplier(WbMethod):
    """
    The method returns a report with [logistics and storage costs
    multiplier](https://seller.wildberries.ru/analytics-reports/dimensions-penalties)

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1analytics~1v1~1measurement-penalties/get
    """

    __return__ = LogisticsAndStorageCostsMultiplierItem
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v1/measurement-penalties"
    __data_key__ = "data.reports"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=1)

    date_from: str | None = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
    limit: int = Field(None)
    offset: int | None = Field(0)
