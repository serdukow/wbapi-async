from pydantic import Field

from ..types.delete_campaign_response import DeleteCampaignResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetDeleteCampaign(WbMethod):
    """
    The method allows to delete campaigns in the status `4` — ready to launch. <br>

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1delete/get
    """

    __return__ = DeleteCampaignResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/delete"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=5)

    id: int = Field(None)
