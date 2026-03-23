from pydantic import Field

from ...types import RequestLimit
from ...types import StopCampaignResponse
from ...methods.base import WbMethod


class GetStopCampaign(WbMethod):
    """
    The method allows to end campaigns in statuses: - `4` — ready to launch - `9` — active - `11` —
    paused

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1stop/get
    """

    __return__ = StopCampaignResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/stop"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: int = Field()
