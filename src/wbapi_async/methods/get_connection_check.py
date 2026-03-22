from ..types.connection_check_response import ConnectionCheckResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetConnectionCheck(WbMethod):
    """
    Checks:

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/WB-API-Connection-Check/paths/~1ping/get
    """

    __return__ = ConnectionCheckResponse
    __api__ = "common-api"
    __method__ = "ping"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
