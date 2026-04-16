from pydantic import Field

from ...types.base import BaseType
from .metrics import Metrics


class SizeDataItem(BaseType):
    """Size Data"""

    region_name: str = Field(alias="regionName")
    office_id: int = Field(alias="officeID")
    office_name: str = Field(alias="officeName")
    metrics: Metrics = Field()
