from pydantic import Field

from ...types.base import BaseType


class Data4(BaseType):
    file_name: str | None = Field(None, alias="fileName")
    extension: str | None = Field(None, alias="extension")
    document: str | None = Field(None, alias="document")
