from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProcessedUploadStateResponse, RequestLimit


class GetProcessedUploadState(WbMethod):
    """
    Returns the processed upload data.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1tasks/get
    """

    __return__ = ProcessedUploadStateResponse
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/history/tasks"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    upload_id: int = Field(alias="uploadID")
