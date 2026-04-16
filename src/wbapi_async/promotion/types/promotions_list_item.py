from pydantic import Field

from ...types.base import BaseType
from ..enums.type__2 import Type2


class PromotionsListItem(BaseType):
    """Promotions List"""

    id_: int | None = Field(None, alias="id")
    name: str | None = Field(None)
    start_date_time: str | None = Field(None, alias="startDateTime")
    end_date_time: str | None = Field(None, alias="endDateTime")
    type_: Type2 | None = Field(None, alias="type")
