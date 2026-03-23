from ...types import ConnectionCheckResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetConnectionCheck(WbMethod):
    """
    Checks: 1. Whether the request successfully reaches the WB API. 2. The validity of the
    authorizationtoken and request URL. 3. Whether the token category matches the service.

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/WB-API-Connection-Check/paths/~1ping/get
    """

    __return__ = ConnectionCheckResponse
    __api__ = "common-api"
    __method__ = "ping"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
