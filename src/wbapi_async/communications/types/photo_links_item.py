from pydantic import Field

from ...types.base import BaseType


class PhotoLinksItem(BaseType):
    full_size: str | None = Field(None, alias="fullSize")
    mini_size: str | None = Field(None, alias="miniSize")
