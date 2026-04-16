from pydantic import Field

from ...types.base import BaseType


class ItemsItem(BaseType):
    advert_id: int = Field()
    nm_id: int = Field()
