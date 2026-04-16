from pydantic import Field

from ...types.base import BaseType
from ..enums.code import Code


class AccessItem(BaseType):
    code: Code = Field()
    disabled: bool = Field()
