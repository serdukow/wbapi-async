from pydantic import Field

from ...types.base import BaseType


class HscodesItem(BaseType):
    """HS-codes"""

    tnved: str | None = Field(None, alias="tnved")
    is_kiz: bool | None = Field(None, alias="isKiz")
