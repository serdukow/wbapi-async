from pydantic import Field

from ...types.base import BaseType


class ModelsVolumeTariff(BaseType):
    from_: int | None = Field(None, alias="from")
    to: int | None = Field(None)
    value: float | None = Field(None)
