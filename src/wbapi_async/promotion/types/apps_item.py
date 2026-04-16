from pydantic import Field

from ...types.base import BaseType
from ..enums.app_type import AppType
from .nms_item import NmsItem


class AppsItem(BaseType):
    app_type: AppType = Field(alias="appType")
    atbs: int = Field()
    canceled: int = Field()
    clicks: int = Field()
    cpc: float = Field()
    cr: float = Field()
    ctr: float = Field()
    nms: list[NmsItem] = Field()
    orders: int = Field()
    shks: int = Field()
    sum_: float = Field(alias="sum")
    sum_price: float = Field()
    views: int = Field()
