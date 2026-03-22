from pydantic import Field

from ..types.selfpurchases_item import SelfpurchasesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSelfpurchases(WbMethod):
    """
    Returns report with self-purchase deductions. The report is generated on Wednesdays at 7:00
    UTC+4and contains weekly data. Also you can get all data starting from August 2023.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1v1~1analytics~1antifraud-details/get
    """

    __return__ = SelfpurchasesItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/antifraud-details"
    __data_key__ = "details"

    request_limit: RequestLimit = RequestLimit(period=600, limit=1, interval=600000, burst=10)

    date: str | None = Field(None)
