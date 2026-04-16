from pydantic import Field

from ...types.base import BaseType


class Order(BaseType):
    """The order of return of batches"""

    ascending: bool | None = Field(None)
