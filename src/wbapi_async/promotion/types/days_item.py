from pydantic import Field

from ...types.base import BaseType
from .apps_item import AppsItem


class DaysItem(BaseType):
    apps: list[AppsItem] = Field(alias="apps")
    atbs: int = Field(alias="atbs")
    canceled: int = Field(alias="canceled")
    date: str = Field(alias="date")
    clicks: int = Field(alias="clicks")
    cpc: float = Field(alias="cpc")
    cr: float = Field(alias="cr")
    ctr: float = Field(alias="ctr")
    orders: int = Field(alias="orders")
    shks: int = Field(alias="shks")
    sum_: float = Field(alias="sum")
    sum_price: float = Field(alias="sum_price")
    views: int = Field(alias="views")
