from pydantic import Field

from ...types.base import BaseType


class PhotosItem(BaseType):
    big: str | None = Field(None, alias="big")
    c246x328: str | None = Field(None, alias="c246x328")
    c516x688: str | None = Field(None, alias="c516x688")
    square: str | None = Field(None, alias="square")
    tm: str | None = Field(None, alias="tm")
