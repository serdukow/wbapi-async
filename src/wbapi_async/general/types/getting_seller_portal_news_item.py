from pydantic import Field

from ...types.base import BaseType
from .types_item import TypesItem


class GettingSellerPortalNewsItem(BaseType):
    """Getting Seller Portal News"""

    content: str | None = Field(None)
    date: str | None = Field(None)
    header: str | None = Field(None)
    id_: int | None = Field(None, alias="id")
    types: list[TypesItem] | None = Field(None)
