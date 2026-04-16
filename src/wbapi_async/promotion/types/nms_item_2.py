from pydantic import Field

from ...types.base import BaseType


class NmsItem2(BaseType):
    atbs: int = Field(alias="atbs")
    canceled: int = Field(alias="canceled")
    clicks: int = Field(alias="clicks")
    cpc: float = Field(alias="cpc")
    cr: float = Field(alias="cr")
    ctr: float = Field(alias="ctr")
    name: str = Field(alias="name")
    nm_id: int = Field(alias="nmId")
    orders: int = Field(alias="orders")
    shks: int = Field(alias="shks")
    sum_: float = Field(alias="sum")
    sum_price: float = Field(alias="sum_price")
    views: int = Field(alias="views")
