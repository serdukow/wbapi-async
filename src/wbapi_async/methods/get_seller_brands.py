from ..types.seller_brands_item import SellerBrandsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSellerBrands(WbMethod):
    """
    Returns the list of the seller brands.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Share-of-Brand-in-Sales/paths/~1api~1v1~1analytics~1brand-share~1brands/get
    """

    __return__ = SellerBrandsItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/brand-share/brands"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=10)
