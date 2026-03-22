from pydantic import Field

from ..types.create_campaign_response import CreateCampaignResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreateCampaign(WbMethod):
    """
    The method creates campaign:

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1adv~1v2~1seacat~1save-ad/post
    """

    __return__ = CreateCampaignResponse
    __api__ = "advert-api"
    __method__ = "adv/v2/seacat/save-ad"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=5, interval=12, burst=5)

    name: str | None = Field(None)
    nms: list[int] | None = Field(None)
    bid_type: str | None = Field("manual")
    payment_type: str | None = Field("cpm")
    placement_types: list[str] | None = Field(['search'])
