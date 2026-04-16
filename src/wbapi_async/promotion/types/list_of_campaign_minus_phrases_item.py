from pydantic import Field

from ...types.base import BaseType


class ListOfCampaignMinusPhrasesItem(BaseType):
    """List of Campaign Minus Phrases"""

    advert_id: int | None = Field(None, alias="advert_id")
    nm_id: int | None = Field(None, alias="nm_id")
    norm_queries: list[str] | None = Field(None, alias="norm_queries")
