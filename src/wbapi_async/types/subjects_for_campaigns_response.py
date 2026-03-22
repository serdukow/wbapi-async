from pydantic import Field

from .base import BaseType


class SubjectsForCampaignsResponse(BaseType):
    """Subjects for Campaigns"""

    id: int | None = Field(None)
    name: str | None = Field(None)
    count: int | None = Field(None)
