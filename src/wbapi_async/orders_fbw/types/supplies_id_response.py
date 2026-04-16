from pydantic import Field

from ...types.base import BaseType


class SuppliesIdResponse(BaseType):
    """Supply Details"""

    phone: str | None = Field(None, alias="phone")
    status_id: int | None = Field(None, alias="statusID")
    virtual_type_id: int | None = Field(None, alias="virtualTypeID")
    box_type_id: int | None = Field(None, alias="boxTypeID")
    create_date: str | None = Field(None, alias="createDate")
    supply_date: str | None = Field(None, alias="supplyDate")
    fact_date: str | None = Field(None, alias="factDate")
    updated_date: str | None = Field(None, alias="updatedDate")
    warehouse_id: int | None = Field(None, alias="warehouseID")
    warehouse_name: str | None = Field(None, alias="warehouseName")
    actual_warehouse_id: int | None = Field(None, alias="actualWarehouseID")
    actual_warehouse_name: str | None = Field(None, alias="actualWarehouseName")
    transit_warehouse_id: int | None = Field(None, alias="transitWarehouseID")
    transit_warehouse_name: str | None = Field(None, alias="transitWarehouseName")
    acceptance_cost: float | None = Field(None, alias="acceptanceCost")
    paid_acceptance_coefficient: float | None = Field(None, alias="paidAcceptanceCoefficient")
    reject_reason: str | None = Field(None, alias="rejectReason")
    supplier_assign_name: str | None = Field(None, alias="supplierAssignName")
    storage_coef: str | None = Field(None, alias="storageCoef")
    delivery_coef: str | None = Field(None, alias="deliveryCoef")
    quantity: int | None = Field(None, alias="quantity")
    ready_for_sale_quantity: int | None = Field(None, alias="readyForSaleQuantity")
    accepted_quantity: int | None = Field(None, alias="acceptedQuantity")
    unloading_quantity: int | None = Field(None, alias="unloadingQuantity")
    depersonalized_quantity: int | None = Field(None, alias="depersonalizedQuantity")
    is_box_on_pallet: bool | None = Field(None, alias="isBoxOnPallet")
