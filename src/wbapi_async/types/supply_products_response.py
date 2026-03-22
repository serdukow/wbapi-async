from pydantic import Field

from .base import BaseType


class SupplyProductsResponse(BaseType):
    """Supply Products"""

    barcode: str | None = Field(None)
    vendor_code: str | None = Field(None, alias="vendorCode")
    nm_id: int | None = Field(None, alias="nmID")
    need_kiz: bool | None = Field(None, alias="needKiz")
    tnved: str | None = Field(None)
    tech_size: str | None = Field(None, alias="techSize")
    color: str | None = Field(None)
    supplier_box_amount: int | None = Field(None, alias="supplierBoxAmount")
    quantity: int | None = Field(None)
    ready_for_sale_quantity: int | None = Field(None, alias="readyForSaleQuantity")
    accepted_quantity: int | None = Field(None, alias="acceptedQuantity")
    unloading_quantity: int | None = Field(None, alias="unloadingQuantity")
