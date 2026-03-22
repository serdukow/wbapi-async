from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import DocumentsResponse, RequestLimit


class GetDocuments(WbMethod):
    """
    Returns more than one document.

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1download~1all/post
    """

    __return__ = DocumentsResponse
    __api__ = "documents-api"
    __method__ = "api/v1/documents/download/all"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    params: list[dict[str, Any]] | None = Field(None)
