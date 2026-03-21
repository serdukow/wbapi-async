from ..types.get_offices_response import GetOfficesResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetOffices(WbMethod):
    """
    Get Offices

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1offices/get
    """

    __return__ = GetOfficesResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/offices"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)
