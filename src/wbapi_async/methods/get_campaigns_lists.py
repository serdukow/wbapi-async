from ..types.campaigns_list import CampaignsList
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetCampaignsLists(WbMethod):
    """
    Returns campaigns lists grouped by type and status.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns/paths/~1adv~1v1~1promotion~1count/get
    """

    __return__ = CampaignsList
    __api__ = "advert-api"
    __method__ = "adv/v1/promotion/count"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=5)
