from ...methods.base import WbMethod
from ...types import CampaignsListsItem, RequestLimit


class GetCampaignsLists(WbMethod):
    """
    Method allows to get campaigns lists grouped by type and status with information about last
    campaignchange date.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns/paths/~1adv~1v1~1promotion~1count/get
    """

    __return__ = CampaignsListsItem
    __api__ = "advert-api"
    __method__ = "adv/v1/promotion/count"
    __data_key__ = "adverts"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
