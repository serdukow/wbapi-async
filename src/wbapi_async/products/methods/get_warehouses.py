from ...methods.base import WbMethod
from ...types import RequestLimit, WarehousesResponse


class GetWarehouses(WbMethod):
    """
    Returns a list of all seller's warehouses.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses/get
    """

    __return__ = WarehousesResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/warehouses"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
