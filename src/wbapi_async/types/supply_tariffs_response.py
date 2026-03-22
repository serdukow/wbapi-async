from pydantic import Field

from .base import BaseType


class SupplyTariffsResponse(BaseType):
    """Supply Tariffs"""

    date: str | None = Field(None)
    coefficient: float | None = Field(None)
    warehouse_id: int | None = Field(None, alias="warehouseID")
    warehouse_name: str | None = Field(None, alias="warehouseName")
    allow_unload: bool | None = Field(None, alias="allowUnload")
    box_type_id: int | None = Field(None, alias="boxTypeID")
    storage_coef: str | None = Field(None, alias="storageCoef")
    delivery_coef: str | None = Field(None, alias="deliveryCoef")
    delivery_base_liter: str | None = Field(None, alias="deliveryBaseLiter")
    delivery_additional_liter: str | None = Field(None, alias="deliveryAdditionalLiter")
    storage_base_liter: str | None = Field(None, alias="storageBaseLiter")
    storage_additional_liter: str | None = Field(None, alias="storageAdditionalLiter")
    is_sorting_center: bool | None = Field(None, alias="isSortingCenter")
