from ..types.offices_for_pass_response import OfficesForPassResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetOfficesForPass(WbMethod):
    """
    Returns a list of offices that require a pass.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes~1offices/get
    """

    __return__ = OfficesForPassResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/passes/offices"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)
