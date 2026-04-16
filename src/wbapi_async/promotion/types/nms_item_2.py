from pydantic import Field

from ...types.base import BaseType


class NmsItem2(BaseType):
    atbs: int = Field()
    canceled: int = Field()
    clicks: int = Field()
    cpc: float = Field()
    cr: float = Field()
    ctr: float = Field()
    name: str = Field()
    nm_id: int = Field(alias="nmId")
    orders: int = Field()
    shks: int = Field()
    sum_: float = Field(alias="sum")
    sum_price: float = Field()
    views: int = Field()
