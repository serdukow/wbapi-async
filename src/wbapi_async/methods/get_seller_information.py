from ..types.seller_information_response import SellerInformationResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSellerInformation(WbMethod):
    """
    This method allows you to obtain the seller's name and account ID.

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-Information/paths/~1api~1v1~1seller-info/get
    """

    __return__ = SellerInformationResponse
    __api__ = "common-api"
    __method__ = "api/v1/seller-info"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=10)
