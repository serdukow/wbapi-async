from pydantic import Field

from ...types.base import BaseType
from .types_item import TypesItem


class GettingSellerPortalNewsItem(BaseType):
    """Getting Seller Portal News"""

    content: str | None = Field(None, alias="content")
    date: str | None = Field(None, alias="date")
    header: str | None = Field(None, alias="header")
    id_: int | None = Field(None, alias="id")
    types: list[TypesItem] | None = Field(None, alias="types")
