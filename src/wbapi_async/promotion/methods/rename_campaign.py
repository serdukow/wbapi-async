from pydantic import Field

from ...methods.base import WbMethod
from ...types import RenameCampaignResponse, RequestLimit


class RenameCampaign(WbMethod):
    """
    The method allows to rename a campaign.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1rename/post
    """

    __return__ = RenameCampaignResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/rename"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    advert_id: int = Field(alias="advertId")
    name: str = Field()
