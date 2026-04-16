from pydantic import Field

from ...types.base import BaseType


class ModelsGoodInBox(BaseType):
    barcode: str | None = Field(None)
    quantity: int | None = Field(None)
