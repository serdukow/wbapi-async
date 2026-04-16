from pydantic import Field

from ...types.base import BaseType


class AccessItem(BaseType):
    code: str = Field(alias="code")
    disabled: bool = Field(alias="disabled")
