from pydantic import Field

from ..types.unprocessed_upload_state_response import UnprocessedUploadStateResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetUnprocessedUploadState(WbMethod):
    """
    Returns the processing upload data.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1buffer~1tasks/get
    """

    __return__ = UnprocessedUploadStateResponse
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/buffer/tasks"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    upload_id: int = Field(None, alias="uploadID")
