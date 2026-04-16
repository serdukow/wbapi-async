from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, TopupOfTheCampaignBudgetResponse


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

    id_: int = Field(alias="id")
    sum_: int | None = Field(None, alias="sum")
    cashback_sum: int | None = Field(None, alias="cashback_sum")
    cashback_percent: int | None = Field(None, alias="cashback_percent")
    type_: int | None = Field(None, alias="type")
    return_: bool | None = Field(None, alias="return")
