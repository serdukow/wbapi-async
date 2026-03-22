from pydantic import Field

from ..types.stop_campaign_response import StopCampaignResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetStopCampaign(WbMethod):
    """
    The method allows to end campaigns in statuses:

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1stop/get
    """

    __return__ = StopCampaignResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/stop"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=5)

    id: int = Field(None)
