from ...methods.base import WbMethod
from ...types import JamSubscriptionInformationResponse, RequestLimit


class GetJamSubscriptionInformation(WbMethod):
    """
    You can get Jam subscription information with a token of any category.

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-Information/paths/~1api~1common~1v1~1subscriptions/get
    """

    __return__ = JamSubscriptionInformationResponse
    __api__ = "common-api"
    __method__ = "api/common/v1/subscriptions"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
