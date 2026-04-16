from pydantic import Field

from ...methods.base import WbMethod
from ...types import ChangingPlacementsInCampaignsWithCustomBidResponse, PlacementsItem, RequestLimit


class ChangingPlacementsInCampaignsWithCustomBid(WbMethod):
    """
    The method allows you to change placements in campaigns with custom bid and per mille payment
    model— `cpm`. For campaigns in statuses `4`, `9` and `11`.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1auction~1placements/put
    """

    __return__ = ChangingPlacementsInCampaignsWithCustomBidResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/auction/placements"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    placements: list[PlacementsItem] = Field()
