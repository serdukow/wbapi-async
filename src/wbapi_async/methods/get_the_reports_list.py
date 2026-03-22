from pydantic import Field

from ..types.the_reports_list_item import TheReportsListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetTheReportsList(WbMethod):
    """
    The method provides a list of reports with advanced seller analytics. The response contains
    [report
    IDs](/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post)and
    generationstatuses.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/get
    """

    __return__ = TheReportsListItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/nm-report/downloads"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    filter_download_ids: list[str] | None = Field(None, alias="filter[downloadIds]")
