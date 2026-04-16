from pydantic import Field

from ...types.base import BaseType


class WarehouseMeasurementsItem(BaseType):
    """Warehouse Measurements"""

    nm_id: int | None = Field(None, alias="nmId")
    subject_name: str | None = Field(None, alias="subjectName")
    dim_id: int | None = Field(None, alias="dimId")
    volume: float | None = Field(None, alias="volume")
    width: int | None = Field(None, alias="width")
    length: int | None = Field(None, alias="length")
    height: int | None = Field(None, alias="height")
    photo_urls: list[str] | None = Field(None, alias="photoUrls")
    dt: str | None = Field(None, alias="dt")
