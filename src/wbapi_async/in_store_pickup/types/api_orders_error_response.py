from pydantic import Field

from ...types.base import BaseType


class ApiOrdersErrorResponse(BaseType):
    code: int = Field()
    detail: str = Field()
