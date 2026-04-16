from pydantic import Field

from ...types.base import BaseType


class PhotosItem(BaseType):
    big: str | None = Field(None)
    c246x328: str | None = Field(None)
    c516x688: str | None = Field(None)
    square: str | None = Field(None)
    tm: str | None = Field(None)
