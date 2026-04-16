from pydantic import Field

from ...types.base import BaseType


class File(BaseType):
    content_type: str | None = Field(None, alias="contentType")
    date: str | None = Field(None, alias="date")
    download_id: str | None = Field(None, alias="downloadID")
    name: str | None = Field(None, alias="name")
    url: str | None = Field(None, alias="url")
    size: int | None = Field(None, alias="size")
