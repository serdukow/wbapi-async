from pydantic import Field

from ...types.base import BaseType


class ModelsDateFilterRequest(BaseType):
    from_: str | None = Field(None, alias="from")
    till: str | None = Field(None, alias="till")
    type_: str = Field(alias="type")
