from pydantic import Field

from ...types.base import BaseType


class Dimensions(BaseType):
    """Dimensions and weight of packed product in cm and kg"""

    length: int | None = Field(None, alias="length")
    width: int | None = Field(None, alias="width")
    height: int | None = Field(None, alias="height")
    weight_brutto: float | None = Field(None, alias="weightBrutto")
    is_valid: bool | None = Field(None, alias="isValid")
