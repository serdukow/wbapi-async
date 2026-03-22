from pydantic import Field

from .base import BaseType


class ListOfCampaignMinusPhrasesItem(BaseType):
    """List of Campaign Minus Phrases"""

    advert_id: int | None = Field(None)
    nm_id: int | None = Field(None)
    norm_queries: list[str] | None = Field(None)
