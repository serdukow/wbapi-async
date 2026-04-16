from pydantic import Field

from ...types.base import BaseType
from .warehouses_item_2 import WarehousesItem2


class WarehouseRemainsTasksTaskIdDownloadResponse(BaseType):
    """Get the Report"""

    brand: str | None = Field(None, alias="brand")
    subject_name: str | None = Field(None, alias="subjectName")
    vendor_code: str | None = Field(None, alias="vendorCode")
    nm_id: int | None = Field(None, alias="nmId")
    barcode: str | None = Field(None, alias="barcode")
    tech_size: str | None = Field(None, alias="techSize")
    volume: float | None = Field(None, alias="volume")
    warehouses: list[WarehousesItem2] | None = Field(None, alias="warehouses")
