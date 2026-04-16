from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProcessedUploadDetailsItem, RequestLimit


class GetProcessedUploadDetails(WbMethod):
    """
    Returns products in processed upload including product errors.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1goods~1task/get
    """

    __return__ = ProcessedUploadDetailsItem
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/history/goods/task"
    __data_key__ = "data.historyGoods"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int = Field(alias="limit")
    offset: int | None = Field(None, alias="offset")
    upload_id: int = Field(alias="uploadID")
