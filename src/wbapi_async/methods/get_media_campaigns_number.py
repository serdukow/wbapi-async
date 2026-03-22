from ..types.media_campaigns_number_response import MediaCampaignsNumberResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetMediaCampaignsNumber(WbMethod):
    """
    Method allows you to get the number of the seller's media campaigns.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Media/paths/~1adv~1v1~1count/get
    """

    __return__ = MediaCampaignsNumberResponse
    __api__ = "advert-media-api"
    __method__ = "adv/v1/count"

    request_limit: RequestLimit = RequestLimit(period=1, limit=10, interval=100, burst=10)
