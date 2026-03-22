from pydantic import Field

from ..types.subjects_for_campaigns_response import SubjectsForCampaignsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSubjectsForCampaigns(WbMethod):
    """
    Returns subjects product cards from which are available for all campaigns

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1adv~1v1~1supplier~1subjects/get
    """

    __return__ = SubjectsForCampaignsResponse
    __api__ = "advert-api"
    __method__ = "adv/v1/supplier/subjects"

    request_limit: RequestLimit = RequestLimit(period=12, limit=1, interval=12, burst=5)

    payment_type: str | None = Field("cpm")
