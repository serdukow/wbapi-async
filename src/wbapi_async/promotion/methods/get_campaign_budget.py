from pydantic import Field

from ...methods.base import WbMethod
from ...types import CampaignBudgetResponse, RequestLimit


class GetCampaignBudget(WbMethod):
    """
    The method allows to get information about the budget of a campaign.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1budget/get
    """

    __return__ = CampaignBudgetResponse
    __api__ = "advert-api"
    __method__ = "adv/v1/budget"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id_: int = Field(alias="id")
