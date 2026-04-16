from pydantic import Field

from ...types.base import BaseType


class WarehousesItem2(BaseType):
    warehouse_name: str | None = Field(None, alias="warehouseName")
    quantity: int | None = Field(None, alias="quantity")
