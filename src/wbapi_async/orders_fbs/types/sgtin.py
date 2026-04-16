from pydantic import Field

from ...types.base import BaseType


class Sgtin(BaseType):
    """Data Matrix code (Chestny ZNAK)"""

    value: list[str] | None = Field(None)
