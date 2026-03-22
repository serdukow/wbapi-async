from pydantic import Field

from ..types.documents_list_item import DocumentsListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetDocumentsList(WbMethod):
    """
    Returns seller's documents list

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1list/get
    """

    __return__ = DocumentsListItem
    __api__ = "documents-api"
    __method__ = "api/v1/documents/list"
    __data_key__ = "data.documents"

    request_limit: RequestLimit = RequestLimit(period=10, limit=1, interval=10, burst=5)

    locale: str | None = Field("en")
    begin_time: str | None = Field(None, alias="beginTime")
    end_time: str | None = Field(None, alias="endTime")
    sort: str | None = Field("date")
    order: str | None = Field("desc")
    category: str | None = Field(None)
    service_name: str | None = Field(None, alias="serviceName")
    limit: int | None = Field(50)
    offset: int | None = Field(0)
