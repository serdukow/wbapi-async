from pydantic import Field

from ..types.unprocessed_upload_details_item import UnprocessedUploadDetailsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetUnprocessedUploadDetails(WbMethod):
    """
    Returns products in processing upload including product errors.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1buffer~1goods~1task/get
    """

    __return__ = UnprocessedUploadDetailsItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/buffer/goods/task"
    __data_key__ = "data.bufferGoods"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    limit: int = Field(None)
    offset: int | None = Field(None)
    upload_id: int = Field(None, alias="uploadID")
