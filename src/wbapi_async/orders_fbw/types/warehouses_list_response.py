from pydantic import Field

from ...types.base import BaseType


class WarehousesListResponse(BaseType):
    """Warehouses List"""

    id_: int | None = Field(None, alias="ID")
    name: str | None = Field(None, alias="name")
    address: str | None = Field(None, alias="address")
    work_time: str | None = Field(None, alias="workTime")
    is_active: bool | None = Field(None, alias="isActive")
    is_transit_active: bool | None = Field(None, alias="isTransitActive")
