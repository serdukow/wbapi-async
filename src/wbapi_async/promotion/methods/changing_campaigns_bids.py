from typing import Any

from pydantic import Field

from ...types import ChangingCampaignsBidsItem
from ...types import RequestLimit
from ...methods.base import WbMethod


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

    bids: list[dict[str, Any]] = Field()
