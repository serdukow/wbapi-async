from pydantic import Field

from .base import BaseType


class WarehouseResponse(BaseType):
    """Warehouse"""

    last_change_date: str | None = Field(None, alias="lastChangeDate")
    warehouse_name: str | None = Field(None, alias="warehouseName")
    supplier_article: str | None = Field(None, alias="supplierArticle")
    nm_id: int | None = Field(None, alias="nmId")
    barcode: str | None = Field(None)
    quantity: int | None = Field(None)
    in_way_to_client: int | None = Field(None, alias="inWayToClient")
    in_way_from_client: int | None = Field(None, alias="inWayFromClient")
    quantity_full: int | None = Field(None, alias="quantityFull")
    category: str | None = Field(None)
    subject: str | None = Field(None)
    brand: str | None = Field(None)
    tech_size: str | None = Field(None, alias="techSize")
    price: float | None = Field(None, alias="Price")
    discount: float | None = Field(None, alias="Discount")
    is_supply: bool | None = Field(None, alias="isSupply")
    is_realization: bool | None = Field(None, alias="isRealization")
    sc_code: str | None = Field(None, alias="SCCode")
