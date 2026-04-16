from pydantic import Field

from ...types.base import BaseType


class V0GetNormQueryStatsItemStat(BaseType):
    norm_query: str | None = Field(None)
    views: int | None = Field(None)
    clicks: int | None = Field(None)
    atbs: int | None = Field(None)
    orders: int | None = Field(None)
    ctr: float | None = Field(None)
    cpc: float | None = Field(None)
    cpm: float | None = Field(None)
    avg_pos: float | None = Field(None)
    shks: int | None = Field(None)
    spend: float | None = Field(None)
