from typing import Any

from pydantic import Field

from ..types.list_of_campaign_minus_phrases_item import ListOfCampaignMinusPhrasesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ListOfCampaignMinusPhrases(WbMethod):
    """
    The method returns a list of minus phrases by:

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1get-minus/post
    """

    __return__ = ListOfCampaignMinusPhrasesItem
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/get-minus"
    __http_method__ = "POST"
    __data_key__ = "items"

    request_limit: RequestLimit = RequestLimit(period=1, limit=5, interval=200, burst=10)

    items: list[Any] = Field(None)
