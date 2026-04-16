from pydantic import Field

from ...types.base import BaseType


class Image(BaseType):
    """Image"""

    date: str | None = Field(None, alias="date")
    download_id: str | None = Field(None, alias="downloadID")
    url: str | None = Field(None, alias="url")
