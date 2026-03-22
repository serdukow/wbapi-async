from ...methods.base import WbMethod
from ...types import PassesResponse, RequestLimit


class GetPasses(WbMethod):
    """
    Returns a list of all seller's passes.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes/get
    """

    __return__ = PassesResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/passes"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
