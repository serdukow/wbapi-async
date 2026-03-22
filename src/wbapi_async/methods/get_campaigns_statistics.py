from pydantic import Field

from ..types.campaigns_statistics_response import CampaignsStatisticsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetCampaignsStatistics(WbMethod):
    """
    The method generates statistics for campaigns, regardless of their type.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v3~1fullstats/get
    """

    __return__ = CampaignsStatisticsResponse
    __api__ = "advert-api"
    __method__ = "adv/v3/fullstats"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=1)

    ids: str = Field(None)
    begin_date: str = Field(None, alias="beginDate")
    end_date: str = Field(None, alias="endDate")
