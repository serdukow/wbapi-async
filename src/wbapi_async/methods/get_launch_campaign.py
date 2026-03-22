from pydantic import Field

from ..types.launch_campaign_response import LaunchCampaignResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetLaunchCampaign(WbMethod):
    """
    The method allows to run campaigns that are in statuses `4` — ready to launch or `11` — paused
    campaign.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1start/get
    """

    __return__ = LaunchCampaignResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/start"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=5)

    id: int = Field(None)
