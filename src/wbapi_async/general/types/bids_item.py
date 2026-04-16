from pydantic import Field

from ...enums import PlacementTypesItem
from ...types.base import BaseType


class BidsItem(BaseType):
    type_: PlacementTypesItem = Field(alias="type")
    value: int = Field()
