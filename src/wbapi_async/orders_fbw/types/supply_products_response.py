from pydantic import Field

from ...types.base import BaseType


class SupplyProductsResponse(BaseType):
    """Supply Products"""

    barcode: str | None = Field(None, alias="barcode")
    vendor_code: str | None = Field(None, alias="vendorCode")
    nm_id: int | None = Field(None, alias="nmID")
    need_kiz: bool | None = Field(None, alias="needKiz")
    tnved: str | None = Field(None, alias="tnved")
    tech_size: str | None = Field(None, alias="techSize")
    color: str | None = Field(None, alias="color")
    supplier_box_amount: int | None = Field(None, alias="supplierBoxAmount")
    quantity: int | None = Field(None, alias="quantity")
    ready_for_sale_quantity: int | None = Field(None, alias="readyForSaleQuantity")
    accepted_quantity: int | None = Field(None, alias="acceptedQuantity")
    unloading_quantity: int | None = Field(None, alias="unloadingQuantity")
