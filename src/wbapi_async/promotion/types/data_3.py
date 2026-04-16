from pydantic import Field

from ...types.base import BaseType


class Data3(BaseType):
    """Response data"""

    already_exists: bool | None = Field(None, alias="alreadyExists")
    upload_id: int | None = Field(None, alias="uploadID")
