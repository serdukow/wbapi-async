from pydantic import Field

from ...methods.base import WbMethod
from ...types import AcceptanceOptionsItem, RequestLimit


class AcceptanceOptions(WbMethod):
    """
    The method returns information about warehouses and package types available for supply. The
    warehouseslist is determined by product's barcode and quantity

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Information-for-Forming-Supplies/paths/~1api~1v1~1acceptance~1options/post
    """

    __return__ = AcceptanceOptionsItem
    __api__ = "supplies-api"
    __method__ = "api/v1/acceptance/options"
    __http_method__ = "POST"
    __data_key__ = "result"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    warehouse_id: int | None = Field(None, alias="warehouseID")
