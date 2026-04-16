from pydantic import Field

from ...types.base import BaseType


class Timestamps(BaseType):
    """Timestamps"""

    created: str = Field()
    updated: str = Field()
    started: str | None = Field(None)
    deleted: str = Field()
