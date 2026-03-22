from typing import Any

from pydantic import Field

from ..types.changing_the_list_of_product_cards_in_campaigns_item import ChangingTheListOfProductCardsInCampaignsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ChangingTheListOfProductCardsInCampaigns(WbMethod):
    """
    The method allows you to add and remove product cards in campaigns.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1auction~1nms/patch
    """

    __return__ = ChangingTheListOfProductCardsInCampaignsItem
    __api__ = "advert-api"
    __method__ = "adv/v0/auction/nms"
    __http_method__ = "PATCH"
    __data_key__ = "nms"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=1)

    nms: list[dict[str, Any]] = Field(None)
