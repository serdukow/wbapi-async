from pydantic import Field

from ...types.base import BaseType


class ReceivingTheHistoryOfAccountTopupsResponse(BaseType):
    """Receiving the History of Account Top-ups"""

    id_: int | None = Field(None, alias="id")
    date: str | None = Field(None, alias="date")
    sum_: int | None = Field(None, alias="sum")
    type_: int | None = Field(None, alias="type")
    status_id: int | None = Field(None, alias="statusId")
    card_status: str | None = Field(None, alias="cardStatus")
