from pydantic import Field

from ...types.base import BaseType


class V0GetNormQueryStatsItemStat(BaseType):
    norm_query: str | None = Field(None, alias="norm_query")
    views: int | None = Field(None, alias="views")
    clicks: int | None = Field(None, alias="clicks")
    atbs: int | None = Field(None, alias="atbs")
    orders: int | None = Field(None, alias="orders")
    ctr: float | None = Field(None, alias="ctr")
    cpc: float | None = Field(None, alias="cpc")
    cpm: float | None = Field(None, alias="cpm")
    avg_pos: float | None = Field(None, alias="avg_pos")
    shks: int | None = Field(None, alias="shks")
    spend: float | None = Field(None, alias="spend")
