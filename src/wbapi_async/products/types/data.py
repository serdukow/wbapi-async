from pydantic import Field

from ...types.base import BaseType


class Data(BaseType):
    free_limits: int | None = Field(None, alias="freeLimits")
    paid_limits: int | None = Field(None, alias="paidLimits")
