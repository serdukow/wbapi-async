from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import Field, TypeAdapter

from ..types.campaign_statistics import CampaignStatistics
from ..types.request_limit import RequestLimit
from .base import WbMethod


if TYPE_CHECKING:
    from ..client.api import WbAPI


class GetCampaignsStatistics(WbMethod):
    """
    Generates statistics for campaigns regardless of their type.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v3~1fullstats/get
    """

    __return__ = CampaignStatistics
    __api__ = "advert-api"
    __method__ = "adv/v3/fullstats"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20000, burst=1)

    ids: list[int] = Field(alias="ids")
    begin_date: str = Field(alias="beginDate")
    end_date: str = Field(alias="endDate")

    async def emit(self, wb_api: WbAPI) -> list[CampaignStatistics]:
        wb_api.session.headers.set_token(wb_api._token)
        url = wb_api.session.build_url(self.__api__, self.__method__)

        params: dict[str, Any] = {
            "ids": ",".join(str(i) for i in self.ids),
            "beginDate": self.begin_date,
            "endDate": self.end_date,
        }
        raw = await wb_api.session.get(url, params=params, limit=self.request_limit)
        return TypeAdapter(list[CampaignStatistics]).validate_python(raw or [])
