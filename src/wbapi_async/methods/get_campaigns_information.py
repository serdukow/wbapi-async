from pydantic import Field

from ..types.campaigns_information_item import CampaignsInformationItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetCampaignsInformation(WbMethod):
    """
    The method returns information about campaigns with standard or custom bid via statuses,
    paymenttypes and IDs.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns/paths/~1api~1advert~1v2~1adverts/get
    """

    __return__ = CampaignsInformationItem
    __api__ = "advert-api"
    __method__ = "api/advert/v2/adverts"
    __data_key__ = "adverts"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=5)

    ids: str | None = Field(None)
    statuses: str | None = Field(None)
    payment_type: str | None = Field(None)
