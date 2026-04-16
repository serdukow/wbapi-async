from pydantic import Field

from ...types.base import BaseType


class Error(BaseType):
    """Error data. If an error is present"""

    title: str | None = Field(None, alias="title")
    detail: str | None = Field(None, alias="detail")
