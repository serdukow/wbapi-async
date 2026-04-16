from pydantic import Field

from ...types.base import BaseType


class ProductCardsForCampaignsResponse(BaseType):
    """Product Cards for Campaigns"""

    title: str | None = Field(None, alias="title")
    nm: int | None = Field(None, alias="nm")
    subject_id: int | None = Field(None, alias="subjectId")
