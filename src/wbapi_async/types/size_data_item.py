from typing import Any

from pydantic import Field

from .base import BaseType


class SizeDataItem(BaseType):
    """Size Data"""

    region_name: str = Field(None, alias="regionName")
    office_id: int = Field(None, alias="officeID")
    office_name: str = Field(None, alias="officeName")
    metrics: Any = Field(None)
