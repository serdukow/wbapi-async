from pydantic import Field

from ...types.base import BaseType


class SubjectsForCampaignsResponse(BaseType):
    """Subjects for Campaigns"""

    id_: int | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")
    count: int | None = Field(None, alias="count")
