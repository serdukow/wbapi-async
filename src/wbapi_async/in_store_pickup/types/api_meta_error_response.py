from pydantic import Field

from ...types.base import BaseType


class ApiMetaErrorResponse(BaseType):
    code: int = Field(alias="code")
    detail: str = Field(alias="detail")
