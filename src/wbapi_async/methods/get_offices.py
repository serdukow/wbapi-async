from ..types.offices_response import OfficesResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetOffices(WbMethod):
    """
    Returns a list of all offices to link to seller warehouse.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1offices/get
    """

    __return__ = OfficesResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/offices"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)
