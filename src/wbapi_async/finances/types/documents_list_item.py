from pydantic import Field

from ...types.base import BaseType


class DocumentsListItem(BaseType):
    """Documents List"""

    service_name: str | None = Field(None, alias="serviceName")
    name: str | None = Field(None)
    category: str | None = Field(None)
    extensions: list[str] | None = Field(None)
    creation_time: str | None = Field(None, alias="creationTime")
    viewed: bool | None = Field(None)
