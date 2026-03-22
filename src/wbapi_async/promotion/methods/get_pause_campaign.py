from pydantic import Field

from ...methods.base import WbMethod
from ...types import PauseCampaignResponse, RequestLimit


class GetPauseCampaign(WbMethod):
    """
    Campaign in status `9` — active — can be paused

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1pause/get
    """

    __return__ = PauseCampaignResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/pause"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: int = Field()
