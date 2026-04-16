from pydantic import Field

from ...types.base import BaseType
from .nms_item_2 import NmsItem2


class AppsItem(BaseType):
    app_type: int = Field(alias="appType")
    atbs: int = Field(alias="atbs")
    canceled: int = Field(alias="canceled")
    clicks: int = Field(alias="clicks")
    cpc: float = Field(alias="cpc")
    cr: float = Field(alias="cr")
    ctr: float = Field(alias="ctr")
    nms: list[NmsItem2] = Field(alias="nms")
    orders: int = Field(alias="orders")
    shks: int = Field(alias="shks")
    sum_: float = Field(alias="sum")
    sum_price: float = Field(alias="sum_price")
    views: int = Field(alias="views")
