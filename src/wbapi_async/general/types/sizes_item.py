from pydantic import Field

from ...types.base import BaseType


class SizesItem(BaseType):
    chrt_id: int | None = Field(None, alias="chrtID")
    tech_size: str | None = Field(None, alias="techSize")
    wb_size: str | None = Field(None, alias="wbSize")
    skus: list[str] | None = Field(None)
