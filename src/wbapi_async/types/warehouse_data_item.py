from typing import Any

from pydantic import Field

from .base import BaseType


class WarehouseDataItem(BaseType):
    """Warehouse Data"""

    region_name: str = Field(None, alias="regionName")
    metrics: Any = Field(None)
    offices: list[dict[str, Any]] = Field(None)
