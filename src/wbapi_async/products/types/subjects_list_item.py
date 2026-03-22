from pydantic import Field

from ...types.base import BaseType


class SubjectsListItem(BaseType):
    """Subjects List"""

    subject_id: int | None = Field(None, alias="subjectID")
    parent_id: int | None = Field(None, alias="parentID")
    subject_name: str | None = Field(None, alias="subjectName")
    parent_name: str | None = Field(None, alias="parentName")
