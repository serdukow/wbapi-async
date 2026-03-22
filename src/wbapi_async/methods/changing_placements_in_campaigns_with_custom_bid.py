from typing import Any

from pydantic import Field

from ..types.changing_placements_in_campaigns_with_custom_bid_response import ChangingPlacementsInCampaignsWithCustomBidResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ChangingPlacementsInCampaignsWithCustomBid(WbMethod):
    """
    The method allows you to change placements in campaigns with custom bid and per mille payment
    model— `cpm`.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1auction~1placements/put
    """

    __return__ = ChangingPlacementsInCampaignsWithCustomBidResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/auction/placements"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=1)

    placements: list[dict[str, Any]] = Field(None)
