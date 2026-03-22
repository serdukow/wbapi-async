from typing import Any

from pydantic import Field

from ..types.documents_response import DocumentsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetDocuments(WbMethod):
    """
    Returns more than one document.

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1download~1all/post
    """

    __return__ = DocumentsResponse
    __api__ = "documents-api"
    __method__ = "api/v1/documents/download/all"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=300, limit=1, interval=300000, burst=5)

    params: list[dict[str, Any]] | None = Field(None)
