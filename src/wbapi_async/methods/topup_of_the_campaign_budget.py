from pydantic import Field

from ..types.topup_of_the_campaign_budget_response import TopupOfTheCampaignBudgetResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class TopupOfTheCampaignBudget(WbMethod):
    """
    The method tops up the campaign
    [budget](/openapi/promotion#tag/Finances/paths/~1adv~1v1~1budget/get).<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1budget~1deposit/post
    """

    __return__ = TopupOfTheCampaignBudgetResponse
    __api__ = "advert-api"
    __method__ = "adv/v1/budget/deposit"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=5)

    id: int = Field(None)
    sum: int | None = Field(None)
    cashback_sum: int | None = Field(None)
    cashback_percent: int | None = Field(None)
    type: int | None = Field(None)
    return_: bool | None = Field(None, alias="return")
