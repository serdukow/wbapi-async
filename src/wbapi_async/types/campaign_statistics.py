from pydantic import Field

from .base import BaseType


class BoosterStat(BaseType):
    avg_position: int | None = Field(None, alias="avg_position")
    date: str | None = Field(None, alias="date")
    nm: int | None = Field(None, alias="nm")


class NmStat(BaseType):
    atbs: int | None = Field(None, alias="atbs")
    canceled: int | None = Field(None, alias="canceled")
    clicks: int | None = Field(None, alias="clicks")
    cpc: float | None = Field(None, alias="cpc")
    cr: float | None = Field(None, alias="cr")
    ctr: float | None = Field(None, alias="ctr")
    name: str | None = Field(None, alias="name")
    nm_id: int | None = Field(None, alias="nmId")
    orders: int | None = Field(None, alias="orders")
    shks: int | None = Field(None, alias="shks")
    sum: float | None = Field(None, alias="sum")
    sum_price: float | None = Field(None, alias="sum_price")
    views: int | None = Field(None, alias="views")


class AppStat(BaseType):
    app_type: int | None = Field(None, alias="appType")
    atbs: int | None = Field(None, alias="atbs")
    canceled: int | None = Field(None, alias="canceled")
    clicks: int | None = Field(None, alias="clicks")
    cpc: float | None = Field(None, alias="cpc")
    cr: float | None = Field(None, alias="cr")
    ctr: float | None = Field(None, alias="ctr")
    nms: list[NmStat] | None = Field(None, alias="nms")
    orders: int | None = Field(None, alias="orders")
    shks: int | None = Field(None, alias="shks")
    sum: float | None = Field(None, alias="sum")
    sum_price: float | None = Field(None, alias="sum_price")
    views: int | None = Field(None, alias="views")


class DayStat(BaseType):
    apps: list[AppStat] | None = Field(None, alias="apps")
    atbs: int | None = Field(None, alias="atbs")
    canceled: int | None = Field(None, alias="canceled")
    clicks: int | None = Field(None, alias="clicks")
    cpc: float | None = Field(None, alias="cpc")
    cr: float | None = Field(None, alias="cr")
    ctr: float | None = Field(None, alias="ctr")
    date: str | None = Field(None, alias="date")
    orders: int | None = Field(None, alias="orders")
    shks: int | None = Field(None, alias="shks")
    sum: float | None = Field(None, alias="sum")
    sum_price: float | None = Field(None, alias="sum_price")
    views: int | None = Field(None, alias="views")


class CampaignStatistics(BaseType):
    advert_id: int | None = Field(None, alias="advertId")
    atbs: int | None = Field(None, alias="atbs")
    booster_stats: list[BoosterStat] | None = Field(None, alias="boosterStats")
    canceled: int | None = Field(None, alias="canceled")
    clicks: int | None = Field(None, alias="clicks")
    cpc: float | None = Field(None, alias="cpc")
    cr: float | None = Field(None, alias="cr")
    ctr: float | None = Field(None, alias="ctr")
    days: list[DayStat] | None = Field(None, alias="days")
    orders: int | None = Field(None, alias="orders")
    shks: int | None = Field(None, alias="shks")
    sum: float | None = Field(None, alias="sum")
    sum_price: float | None = Field(None, alias="sum_price")
    views: int | None = Field(None, alias="views")
