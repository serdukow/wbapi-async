from typing import Any

from pydantic import Field

from ...types.base import BaseType


class WarehouseDataItem(BaseType):
    """Warehouse Data"""

    region_name: str = Field(alias="regionName")
    metrics: Any = Field()
    offices: list[dict[str, Any]] = Field()
