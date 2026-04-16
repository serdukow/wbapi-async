from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, WarehouseResponse


class GetWarehouse(WbMethod):
    """
    This method is deprecated. It will be removed on [June
    23](https://dev.wildberries.ru/en/release-notes?id=494)

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1stocks/get
    """

    __return__ = WarehouseResponse
    __api__ = "statistics-api"
    __method__ = "api/v1/supplier/stocks"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
