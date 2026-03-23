from pydantic import Field

from ...types import RequestLimit
from ...types import TopupOfTheCampaignBudgetResponse
from ...methods.base import WbMethod


class TopupOfTheCampaignBudget(WbMethod):
    """
    The method tops up the campaign
    [budget](/openapi/promotion#tag/Finances/paths/~1adv~1v1~1budget/get).To launch the campaign
    aftertopping up the budget, use the [Launch
    campaign](/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1start/get)method.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1budget~1deposit/post
    """

    __return__ = TopupOfTheCampaignBudgetResponse
    __api__ = "advert-api"
    __method__ = "adv/v1/budget/deposit"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: int = Field()
    sum: int | None = Field(None)
    cashback_sum: int | None = Field(None)
    cashback_percent: int | None = Field(None)
    type: int | None = Field(None)
    return_: bool | None = Field(None, alias="return")
