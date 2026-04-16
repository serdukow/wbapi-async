from pydantic import Field

from ...types.base import BaseType
from .error import Error
from .warehouses_item import WarehousesItem


class AcceptanceOptionsItem(BaseType):
    """Acceptance Options"""

    barcode: str | None = Field(None)
    error: Error | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    warehouses: list[WarehousesItem] | None = Field(None)
