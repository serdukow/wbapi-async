from pydantic import Field

from ..types.warehouse_response import WarehouseResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetWarehouse(WbMethod):
    """
    The method returns WB warehouses inventory.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1stocks/get
    """

    __return__ = WarehouseResponse
    __api__ = "statistics-api"
    __method__ = "api/v1/supplier/stocks"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=1, burst=1)

    date_from: str = Field(None, alias="dateFrom")
