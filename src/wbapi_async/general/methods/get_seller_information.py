from ...methods.base import WbMethod
from ...types import RequestLimit, SellerInformationResponse


class GetSellerInformation(WbMethod):
    """
    You can get seller information with a token of any category.

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-Information/paths/~1api~1v1~1seller-info/get
    """

    __return__ = SellerInformationResponse
    __api__ = "common-api"
    __method__ = "api/v1/seller-info"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
