from pydantic import Field

from ...types.base import BaseType


class WbWarehousesInventoryItem(BaseType):
    """WB Warehouses Inventory"""

    nm_id: int = Field(alias="nmId")
    chrt_id: int = Field(alias="chrtId")
    warehouse_id: int = Field(alias="warehouseId")
    warehouse_name: str = Field(alias="warehouseName")
    region_name: str = Field(alias="regionName")
    quantity: int = Field()
    in_way_to_client: int = Field(alias="inWayToClient")
    in_way_from_client: int = Field(alias="inWayFromClient")
