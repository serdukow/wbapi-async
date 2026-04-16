from pydantic import Field

from ...types.base import BaseType
from .metrics import Metrics
from .offices_item import OfficesItem


class WarehouseDataItem(BaseType):
    """Warehouse Data"""

    region_name: str = Field(alias="regionName")
    metrics: Metrics = Field()
    offices: list[OfficesItem] = Field()
