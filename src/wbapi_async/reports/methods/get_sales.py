from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SalesResponse


class GetSales(WbMethod):
    """
    The method returns sale and return information. The data updated every 30 minutes.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1sales/get
    """

    __return__ = SalesResponse
    __api__ = "statistics-api"
    __method__ = "api/v1/supplier/sales"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    flag: int | None = Field(0, alias="flag")
