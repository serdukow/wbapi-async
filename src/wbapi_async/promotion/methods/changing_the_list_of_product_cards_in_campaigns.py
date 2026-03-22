from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import ChangingTheListOfProductCardsInCampaignsItem, RequestLimit


class ChangingTheListOfProductCardsInCampaigns(WbMethod):
    """
    The method allows you to add and remove product cards in campaigns. For campaigns in statuses
    `4`,`9` and `11`. The current minimum bid is set for the added products.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1auction~1nms/patch
    """

    __return__ = ChangingTheListOfProductCardsInCampaignsItem
    __api__ = "advert-api"
    __method__ = "adv/v0/auction/nms"
    __http_method__ = "PATCH"
    __data_key__ = "nms"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nms: list[dict[str, Any]] = Field()
