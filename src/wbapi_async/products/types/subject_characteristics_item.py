from pydantic import Field

from ...types.base import BaseType


class SubjectCharacteristicsItem(BaseType):
    """Subject Characteristics"""

    charc_id: int | None = Field(None, alias="charcID")
    subject_name: str | None = Field(None, alias="subjectName")
    subject_id: int | None = Field(None, alias="subjectID")
    name: str | None = Field(None)
    required: bool | None = Field(None)
    unit_name: str | None = Field(None, alias="unitName")
    max_count: int | None = Field(None, alias="maxCount")
    popular: bool | None = Field(None)
    charc_type: int | None = Field(None, alias="charcType")
