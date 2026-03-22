from pydantic import Field

from ..types.report_on_products_with_mandatory_labeling_item import ReportOnProductsWithMandatoryLabelingItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=300, limit=10, interval=1800000, burst=10)

    date_from: str = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
    countries: list[str] | None = Field(None)
