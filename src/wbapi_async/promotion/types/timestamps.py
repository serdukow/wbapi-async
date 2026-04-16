from pydantic import Field

from ...types.base import BaseType


class Timestamps(BaseType):
    """Timestamps"""

    created: str = Field(alias="created")
    updated: str = Field(alias="updated")
    started: str | None = Field(None, alias="started")
    deleted: str = Field(alias="deleted")
