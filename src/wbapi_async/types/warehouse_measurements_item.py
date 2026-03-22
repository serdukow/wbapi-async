from pydantic import Field

from .base import BaseType


class WarehouseMeasurementsItem(BaseType):
    """Warehouse Measurements"""

    nm_id: int | None = Field(None, alias="nmId")
    subject_name: str | None = Field(None, alias="subjectName")
    dim_id: int | None = Field(None, alias="dimId")
    volume: float | None = Field(None)
    width: int | None = Field(None)
    length: int | None = Field(None)
    height: int | None = Field(None)
    photo_urls: list[str] | None = Field(None, alias="photoUrls")
    dt: str | None = Field(None)
