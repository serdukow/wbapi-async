from pydantic import Field

from ...methods.base import WbMethod
from ...types import BidsItem2, ChangingCampaignsBidsItem, RequestLimit


class ChangingCampaignsBids(WbMethod):
    """
    The method changes the bids of product cards by WB articles in campaigns: - with standard bid -
    withcustom bid - with a `cpc` payment model — per click

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1api~1advert~1v1~1bids/patch
    """

    __return__ = ChangingCampaignsBidsItem
    __api__ = "advert-api"
    __method__ = "api/advert/v1/bids"
    __http_method__ = "PATCH"
    __data_key__ = "bids"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    bids: list[BidsItem2] = Field()
