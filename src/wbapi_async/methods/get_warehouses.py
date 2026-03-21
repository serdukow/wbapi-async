from ..types.request_limit import RequestLimit
from ..types.warehouses_response import WarehousesResponse
from .base import WbMethod


class GetWarehouses(WbMethod):
    """
    Returns a list of all seller's warehouses.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses/get
    """

    __return__ = WarehousesResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/warehouses"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)
