from pydantic import Field

from ...types.base import BaseType


class V0GetNormQueryListResponseItemNormQueries(BaseType):
    """Search clusters"""

    active: list[str] | None = Field(None)
    excluded: list[str] | None = Field(None)
