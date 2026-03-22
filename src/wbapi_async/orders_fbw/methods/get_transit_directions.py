from ...methods.base import WbMethod
from ...types import RequestLimit, TransitDirectionsResponse


class GetTransitDirections(WbMethod):
    """
    The method returns information about available transit directions.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Information-for-Forming-Supplies/paths/~1api~1v1~1transit-tariffs/get
    """

    __return__ = TransitDirectionsResponse
    __api__ = "supplies-api"
    __method__ = "api/v1/transit-tariffs"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
