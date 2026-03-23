from pydantic import Field

from ...types import DocumentResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetDocument(WbMethod):
    """
    Returns one document

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1download/get
    """

    __return__ = DocumentResponse
    __api__ = "documents-api"
    __method__ = "api/v1/documents/download"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    service_name: str = Field(alias="serviceName")
    extension: str = Field()
