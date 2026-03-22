from ...methods.base import WbMethod
from ...types import MediaCampaignsNumberResponse, RequestLimit


class GetMediaCampaignsNumber(WbMethod):
    """
    Method allows you to get the number of the seller's media campaigns.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Media/paths/~1adv~1v1~1count/get
    """

    __return__ = MediaCampaignsNumberResponse
    __api__ = "advert-media-api"
    __method__ = "adv/v1/count"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
