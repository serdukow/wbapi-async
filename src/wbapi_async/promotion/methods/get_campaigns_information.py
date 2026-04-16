from pydantic import Field

from ...methods.base import WbMethod
from ...types import CampaignsInformationItem, RequestLimit
from ..enums.payment_type import PaymentType


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    ids: str | None = Field(None)
    statuses: str | None = Field(None)
    payment_type: PaymentType | None = Field(None)
