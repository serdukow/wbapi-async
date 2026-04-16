from pydantic import Field

from ...types.base import BaseType
from ..enums.placement_types_item import PlacementTypesItem


class BidsItem(BaseType):
    type_: PlacementTypesItem = Field(alias="type")
    value: int = Field()
