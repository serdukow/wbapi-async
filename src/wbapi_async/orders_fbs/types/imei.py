from pydantic import Field

from ...types.base import BaseType


class Imei(BaseType):
    """IMEI"""

    value: str | None = Field(None)
