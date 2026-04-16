from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SelfpurchasesItem


class GetSelfpurchases(WbMethod):
    """
    Returns report with self-purchase deductions. The report is generated on Wednesdays at 7:00
    UTC+4and contains weekly data. Also you can get all data starting from August 2023.
    Self-purchasededuction is 30% of product price. Minimum deduction is 100,000 ₽, if the total
    productcost delivered to the pick-up point is more than 100,000 ₽ per one week.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1v1~1analytics~1antifraud-details/get
    """

    __return__ = SelfpurchasesItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/antifraud-details"
    __data_key__ = "details"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date: str | None = Field(None, alias="date")
