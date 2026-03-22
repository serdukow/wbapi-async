from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import ListOfCampaignMinusPhrasesItem, RequestLimit


class ListOfCampaignMinusPhrases(WbMethod):
    """
    The method returns a list of minus phrases by: - campaign IDs - WB articles

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1get-minus/post
    """

    __return__ = ListOfCampaignMinusPhrasesItem
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/get-minus"
    __http_method__ = "POST"
    __data_key__ = "items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    items: list[Any] = Field()
