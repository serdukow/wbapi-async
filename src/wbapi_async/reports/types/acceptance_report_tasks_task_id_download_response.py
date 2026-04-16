from pydantic import Field

from ...types.base import BaseType


class AcceptanceReportTasksTaskIdDownloadResponse(BaseType):
    """Get the Report"""

    count: int | None = Field(None, alias="count")
    gi_create_date: str | None = Field(None, alias="giCreateDate")
    income_id: int | None = Field(None, alias="incomeId")
    nm_id: int | None = Field(None, alias="nmID")
    shk_create_date: str | None = Field(None, alias="shkCreateDate")
    subject_name: str | None = Field(None, alias="subjectName")
    total: float | None = Field(None, alias="total")
