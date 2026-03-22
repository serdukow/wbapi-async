from pydantic import Field

from .base import BaseType


class WarehousesListResponse(BaseType):
    """Warehouses List"""

    id: int | None = Field(None, alias="ID")
    name: str | None = Field(None)
    address: str | None = Field(None)
    work_time: str | None = Field(None, alias="workTime")
    is_active: bool | None = Field(None, alias="isActive")
    is_transit_active: bool | None = Field(None, alias="isTransitActive")
