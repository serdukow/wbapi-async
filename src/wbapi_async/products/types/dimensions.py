from pydantic import Field

from ...types.base import BaseType


class Dimensions(BaseType):
    """Dimensions and weight of packed product in cm and kg"""

    length: int | None = Field(None)
    width: int | None = Field(None)
    height: int | None = Field(None)
    weight_brutto: float | None = Field(None, alias="weightBrutto")
    is_valid: bool | None = Field(None, alias="isValid")
