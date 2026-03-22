from ..types.passes_response import PassesResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetPasses(WbMethod):
    """
    Returns a list of all seller's passes.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes/get
    """

    __return__ = PassesResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/passes"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)
