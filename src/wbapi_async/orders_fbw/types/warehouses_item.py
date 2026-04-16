from pydantic import Field

from ...types.base import BaseType


class WarehousesItem(BaseType):
    warehouse_id: int | None = Field(None, alias="warehouseID")
    can_box: bool | None = Field(None, alias="canBox")
    can_monopallet: bool | None = Field(None, alias="canMonopallet")
    can_supersafe: bool | None = Field(None, alias="canSupersafe")
    is_box_on_pallet: bool | None = Field(None, alias="isBoxOnPallet")
