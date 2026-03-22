from pydantic import Field

from ...types.base import BaseType


class TheReportsListItem(BaseType):
    """Get the Reports List"""

    id: str = Field()
    created_at: str = Field(alias="createdAt")
    status: str = Field()
    name: str = Field()
    size: int = Field()
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
