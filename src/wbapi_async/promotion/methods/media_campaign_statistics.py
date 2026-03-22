from ...methods.base import WbMethod
from ...types import MediaCampaignStatisticsResponse, RequestLimit


class MediaCampaignStatistics(WbMethod):
    """
    The method allows to get statistics of [WB Media](https://cmp.wildberries.ru/cmpf/statistics)
    campaigns

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v1~1stats/post
    """

    __return__ = MediaCampaignStatisticsResponse
    __api__ = "advert-media-api"
    __method__ = "adv/v1/stats"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
