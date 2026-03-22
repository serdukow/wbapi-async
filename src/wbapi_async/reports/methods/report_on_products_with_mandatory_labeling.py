from pydantic import Field

from ...methods.base import WbMethod
from ...types import ReportOnProductsWithMandatoryLabelingItem, RequestLimit


class ReportOnProductsWithMandatoryLabeling(WbMethod):
    """
    Returns operations with labeled products

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Report-on-Products-with-Mandatory-Labeling/paths/~1api~1v1~1analytics~1excise-report/post
    """

    __return__ = ReportOnProductsWithMandatoryLabelingItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/excise-report"
    __http_method__ = "POST"
    __data_key__ = "response.data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    countries: list[str] | None = Field(None)
