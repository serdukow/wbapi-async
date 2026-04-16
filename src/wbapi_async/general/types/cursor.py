from pydantic import Field

from ...types.base import BaseType


class Cursor(BaseType):
    """Cursor"""

    limit: int | None = Field(None)
    updated_at: str | None = Field(None, alias="updatedAt")
    nm_id: int | None = Field(None, alias="nmID")
