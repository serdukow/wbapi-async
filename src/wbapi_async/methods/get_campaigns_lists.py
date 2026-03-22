from ..types.campaigns_lists_item import CampaignsListsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=5)
