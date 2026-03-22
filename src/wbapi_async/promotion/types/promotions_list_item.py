from pydantic import Field

from ...types.base import BaseType


class PromotionsListItem(BaseType):
    """Promotions List"""

    id: int | None = Field(None)
    name: str | None = Field(None)
    start_date_time: str | None = Field(None, alias="startDateTime")
    end_date_time: str | None = Field(None, alias="endDateTime")
    type: str | None = Field(None)
