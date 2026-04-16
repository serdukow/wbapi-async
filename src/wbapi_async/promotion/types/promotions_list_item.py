from pydantic import Field

from ...types.base import BaseType


class PromotionsListItem(BaseType):
    """Promotions List"""

    id_: int | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")
    start_date_time: str | None = Field(None, alias="startDateTime")
    end_date_time: str | None = Field(None, alias="endDateTime")
    type_: str | None = Field(None, alias="type")
