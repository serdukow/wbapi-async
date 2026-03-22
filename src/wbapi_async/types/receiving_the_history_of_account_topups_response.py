from pydantic import Field

from .base import BaseType


class ReceivingTheHistoryOfAccountTopupsResponse(BaseType):
    """Receiving the History of Account Top-ups"""

    id: int | None = Field(None)
    date: str | None = Field(None)
    sum: int | None = Field(None)
    type: int | None = Field(None)
    status_id: int | None = Field(None, alias="statusId")
    card_status: str | None = Field(None, alias="cardStatus")
