from ...methods.base import WbMethod
from ...types import RequestLimit, WarehousesListResponse


class GetWarehousesList(WbMethod):
    """
    The method returns Wildberries warehouses list.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Information-for-Forming-Supplies/paths/~1api~1v1~1warehouses/get
    """

    __return__ = WarehousesListResponse
    __api__ = "supplies-api"
    __method__ = "api/v1/warehouses"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
