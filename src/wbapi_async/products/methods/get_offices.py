from ...types import OfficesResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetOffices(WbMethod):
    """
    Returns a list of all offices to link to seller warehouse.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1offices/get
    """

    __return__ = OfficesResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/offices"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
