from pydantic import Field

from ...methods.base import WbMethod
from ...types import LogisticsAndStorageCostsMultiplierItem, RequestLimit


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
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str | None = Field(None, alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int = Field()
    offset: int | None = Field(0)
