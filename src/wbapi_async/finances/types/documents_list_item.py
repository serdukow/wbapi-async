from pydantic import Field

from ...types.base import BaseType


class DocumentsListItem(BaseType):
    """Documents List"""

    service_name: str | None = Field(None, alias="serviceName")
    name: str | None = Field(None, alias="name")
    category: str | None = Field(None, alias="category")
    extensions: list[str] | None = Field(None, alias="extensions")
    creation_time: str | None = Field(None, alias="creationTime")
    viewed: bool | None = Field(None, alias="viewed")
