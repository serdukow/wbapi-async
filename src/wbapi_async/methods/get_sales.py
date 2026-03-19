from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.sale import Sale
from .base import WbMethod


class GetSales(WbMethod):
    """
    Returns sale and return information.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1sales/get
    """

    __return__ = Sale
    __api__ = "statistics-api"
    __method__ = "api/v1/supplier/sales"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=1)

    date_from: str = Field(alias="dateFrom")
    flag: int = Field(0, alias="flag")

    @property
    def __cursor_field__(self) -> str | None:
        return "lastChangeDate" if self.flag != 1 else None
