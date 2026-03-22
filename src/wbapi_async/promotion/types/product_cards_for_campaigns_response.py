from pydantic import Field

from ...types.base import BaseType


class ProductCardsForCampaignsResponse(BaseType):
    """Product Cards for Campaigns"""

    title: str | None = Field(None)
    nm: int | None = Field(None)
    subject_id: int | None = Field(None, alias="subjectId")
