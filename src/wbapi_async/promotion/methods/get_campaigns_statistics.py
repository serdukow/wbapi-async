from pydantic import Field

from ...methods.base import WbMethod
from ...types import CampaignsStatisticsResponse, RequestLimit


class GetCampaignsStatistics(WbMethod):
    """
    The method generates statistics for campaigns, regardless of their type. The maximum period in
    arequest is 31 days. For campaigns in statuses `7`, `9` and `11`.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v3~1fullstats/get
    """

    __return__ = CampaignsStatisticsResponse
    __api__ = "advert-api"
    __method__ = "adv/v3/fullstats"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    ids: str = Field(alias="ids")
    begin_date: str = Field(alias="beginDate")
    end_date: str = Field(alias="endDate")
