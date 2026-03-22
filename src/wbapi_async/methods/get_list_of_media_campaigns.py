from pydantic import Field

from ..types.list_of_media_campaigns_response import ListOfMediaCampaignsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetListOfMediaCampaigns(WbMethod):
    """
    The method allows to get the list of media campaigns of the seller

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Media/paths/~1adv~1v1~1adverts/get
    """

    __return__ = ListOfMediaCampaignsResponse
    __api__ = "advert-media-api"
    __method__ = "adv/v1/adverts"

    request_limit: RequestLimit = RequestLimit(period=1, limit=10, interval=100, burst=10)

    status: int | None = Field(None)
    type: int | None = Field(None)
    limit: int | None = Field(None)
    offset: int | None = Field(None)
    order: str | None = Field(None)
    direction: str | None = Field(None)
