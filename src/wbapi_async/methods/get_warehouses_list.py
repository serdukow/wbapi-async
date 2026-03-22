from ..types.warehouses_list_response import WarehousesListResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetWarehousesList(WbMethod):
    """
    The method returns Wildberries warehouses list.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Information-for-Forming-Supplies/paths/~1api~1v1~1warehouses/get
    """

    __return__ = WarehousesListResponse
    __api__ = "supplies-api"
    __method__ = "api/v1/warehouses"

    request_limit: RequestLimit = RequestLimit(period=60, limit=6, interval=10, burst=6)
