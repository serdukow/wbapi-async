from ...methods.base import WbMethod
from ...types import ProductCardsForCampaignsResponse, RequestLimit


class ProductCardsForCampaigns(WbMethod):
    """
    Returns product cards that are available for all campaigns.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1adv~1v2~1supplier~1nms/post
    """

    __return__ = ProductCardsForCampaignsResponse
    __api__ = "advert-api"
    __method__ = "adv/v2/supplier/nms"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
