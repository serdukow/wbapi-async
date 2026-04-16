from pydantic import Field

from ...types.base import BaseType
from .cursor import Cursor
from .filter_ import Filter
from .sort import Sort


class Settings(BaseType):
    """Settings"""

    sort: Sort | None = Field(None)
    filter_: Filter | None = Field(None, alias="filter")
    cursor: Cursor | None = Field(None)
