from pydantic import Field

from ...methods.base import WbMethod
from ...types import LaunchCampaignResponse, RequestLimit


class GetLaunchCampaign(WbMethod):
    """
    The method allows to run campaigns that are in statuses `4` — ready to launch or `11` — paused
    campaign.To run a campaign, check its budget. If the budget is insufficient, replenish it.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1start/get
    """

    __return__ = LaunchCampaignResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/start"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id_: int = Field(alias="id")
