from pydantic import Field

from ...types.base import BaseType
from .apps_item import AppsItem


class DaysItem(BaseType):
    apps: list[AppsItem] = Field()
    atbs: int = Field()
    canceled: int = Field()
    date: str = Field()
    clicks: int = Field()
    cpc: float = Field()
    cr: float = Field()
    ctr: float = Field()
    orders: int = Field()
    shks: int = Field()
    sum_: float = Field(alias="sum")
    sum_price: float = Field()
    views: int = Field()
