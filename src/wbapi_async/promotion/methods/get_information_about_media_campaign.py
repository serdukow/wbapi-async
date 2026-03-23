from pydantic import Field

from ...types import InformationAboutMediaCampaignItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetInformationAboutMediaCampaign(WbMethod):
    """
    The method allows to get information about a media campaign

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Media/paths/~1adv~1v1~1advert/get
    """

    __return__ = InformationAboutMediaCampaignItem
    __api__ = "advert-media-api"
    __method__ = "adv/v1/advert"
    __data_key__ = "items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: int = Field()
