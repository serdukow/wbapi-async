from pydantic import Field

from ...types.base import BaseType
from .models_volume_tariff import ModelsVolumeTariff


class TransitDirectionsResponse(BaseType):
    """Transit Directions"""

    transit_warehouse_name: str | None = Field(None, alias="transitWarehouseName")
    destination_warehouse_name: str | None = Field(None, alias="destinationWarehouseName")
    active_from: str | None = Field(None, alias="activeFrom")
    box_tariff: list[ModelsVolumeTariff] | None = Field(None, alias="boxTariff")
    pallet_tariff: int | None = Field(None, alias="palletTariff")
