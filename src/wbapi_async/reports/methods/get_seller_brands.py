from ...methods.base import WbMethod
from ...types import RequestLimit, SellerBrandsItem


class GetSellerBrands(WbMethod):
    """
    Returns the list of the seller brands.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Share-of-Brand-in-Sales/paths/~1api~1v1~1analytics~1brand-share~1brands/get
    """

    __return__ = SellerBrandsItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/brand-share/brands"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
