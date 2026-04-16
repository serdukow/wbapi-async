from pydantic import Field

from ...types.base import BaseType


class TheReportsListItem(BaseType):
    """Get the Reports List"""

    id_: str = Field(alias="id")
    created_at: str = Field(alias="createdAt")
    status: str = Field(alias="status")
    name: str = Field(alias="name")
    size: int = Field(alias="size")
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
