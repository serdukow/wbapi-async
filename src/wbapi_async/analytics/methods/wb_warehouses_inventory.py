from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, WbWarehousesInventoryItem


class WbWarehousesInventory(WbMethod):
    """
    Method is available by token types : Personal , Service

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1analytics~1v1~1stocks-report~1wb-warehouses/post
    """

    __return__ = WbWarehousesInventoryItem
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v1/stocks-report/wb-warehouses"
    __http_method__ = "POST"
    __data_key__ = "data.items"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nm_ids: list[int] | None = Field(None, alias="nmIds")
    chrt_ids: list[int] | None = Field(None, alias="chrtIds")
    limit: int | None = Field(250000)
    offset: int | None = Field(0)
