from pydantic import Field

from ..types.acceptance_options_item import AcceptanceOptionsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=6, interval=10, burst=6)

    warehouse_id: int | None = Field(None, alias="warehouseID")
