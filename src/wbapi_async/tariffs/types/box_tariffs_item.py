from pydantic import Field

from ...types.base import BaseType


class BoxTariffsItem(BaseType):
    """Box Tariffs"""

    box_delivery_base: str | None = Field(None, alias="boxDeliveryBase")
    box_delivery_coef_expr: str | None = Field(None, alias="boxDeliveryCoefExpr")
    box_delivery_liter: str | None = Field(None, alias="boxDeliveryLiter")
    box_delivery_marketplace_base: str | None = Field(None, alias="boxDeliveryMarketplaceBase")
    box_delivery_marketplace_coef_expr: str | None = Field(None, alias="boxDeliveryMarketplaceCoefExpr")
    box_delivery_marketplace_liter: str | None = Field(None, alias="boxDeliveryMarketplaceLiter")
    box_storage_base: str | None = Field(None, alias="boxStorageBase")
    box_storage_coef_expr: str | None = Field(None, alias="boxStorageCoefExpr")
    box_storage_liter: str | None = Field(None, alias="boxStorageLiter")
    geo_name: str | None = Field(None, alias="geoName")
    warehouse_name: str | None = Field(None, alias="warehouseName")
