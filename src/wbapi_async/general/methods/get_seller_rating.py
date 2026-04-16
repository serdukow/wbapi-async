from ...methods.base import WbMethod
from ...types import RequestLimit, SellerRatingResponse


class GetSellerRating(WbMethod):
    """
    To access the method, use a token for the Feedbacks and Questions category

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-Information/paths/~1api~1common~1v1~1rating/get
    """

    __return__ = SellerRatingResponse
    __api__ = "feedbacks-api"
    __method__ = "api/common/v1/rating"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
