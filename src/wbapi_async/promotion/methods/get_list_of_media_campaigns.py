from pydantic import Field

from ...methods.base import WbMethod
from ...types import ListOfMediaCampaignsResponse, RequestLimit


class GetListOfMediaCampaigns(WbMethod):
    """
    The method allows to get the list of media campaigns of the seller

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Media/paths/~1adv~1v1~1adverts/get
    """

    __return__ = ListOfMediaCampaignsResponse
    __api__ = "advert-media-api"
    __method__ = "adv/v1/adverts"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    status: int | None = Field(None, alias="status")
    type_: int | None = Field(None, alias="type")
    limit: int | None = Field(None, alias="limit")
    offset: int | None = Field(None, alias="offset")
    order: str | None = Field(None, alias="order")
    direction: str | None = Field(None, alias="direction")
