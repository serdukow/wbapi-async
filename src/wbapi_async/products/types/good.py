from pydantic import Field

from ...types.base import BaseType


class Good(BaseType):
    nm_id: int = Field(alias="nmID")
    price: int | None = Field(None)
    discount: int | None = Field(None)
