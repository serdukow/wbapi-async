from pydantic import Field

from .base import BaseType


class TheReportsListItem(BaseType):
    """Get the Reports List"""

    id: str = Field(None)
    created_at: str = Field(None, alias="createdAt")
    status: str = Field(None)
    name: str = Field(None)
    size: int = Field(None)
    start_date: str = Field(None, alias="startDate")
    end_date: str = Field(None, alias="endDate")
