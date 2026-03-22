from pydantic import Field

from .base import BaseType


class PalletTariffsItem(BaseType):
    """Pallet Tariffs"""

    pallet_delivery_expr: str | None = Field(None, alias="palletDeliveryExpr")
    pallet_delivery_value_base: str | None = Field(None, alias="palletDeliveryValueBase")
    pallet_delivery_value_liter: str | None = Field(None, alias="palletDeliveryValueLiter")
    pallet_storage_expr: str | None = Field(None, alias="palletStorageExpr")
    pallet_storage_value_expr: str | None = Field(None, alias="palletStorageValueExpr")
    warehouse_name: str | None = Field(None, alias="warehouseName")
