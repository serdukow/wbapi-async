from pydantic import Field

from ...types.base import BaseType


class ASuppliesListItem(BaseType):
    """Get a Supplies List"""

    id_: str | None = Field(None, alias="id")
    is_b2b: bool | None = Field(None, alias="isB2b")
    done: bool | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    closed_at: str | None = Field(None, alias="closedAt")
    scan_dt: str | None = Field(None, alias="scanDt")
    name: str | None = Field(None)
    cargo_type: int | None = Field(None, alias="cargoType")
    cross_border_type: int | None = Field(None, alias="crossBorderType")
    destination_office_id: int | None = Field(None, alias="destinationOfficeId")
