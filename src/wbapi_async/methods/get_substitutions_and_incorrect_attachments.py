from pydantic import Field

from ..types.substitutions_and_incorrect_attachments_item import SubstitutionsAndIncorrectAttachmentsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSubstitutionsAndIncorrectAttachments(WbMethod):
    """
    The method returns a report with [substitutions and incorrect
    attachments](https://seller.wildberries.ru/analytics-reports/dimensions-penalties/retentions)
    retentions

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1analytics~1v1~1deductions/get
    """

    __return__ = SubstitutionsAndIncorrectAttachmentsItem
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v1/deductions"
    __data_key__ = "data.reports"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=1)

    date_from: str | None = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
    sort: str | None = Field("dtBonus")
    order: str | None = Field("desc")
    limit: int = Field(None)
    offset: int | None = Field(0)
