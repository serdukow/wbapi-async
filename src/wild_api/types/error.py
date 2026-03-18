from pydantic import Field

from .base import BaseType


class Error(BaseType):
    data: str | None = Field(None, alias="data")
    error: bool | None = Field(None, alias="error")
    error_text: str | None = Field(None, alias="errorText")
    title: str | None = Field(None, alias="title")
    detail: str | None = Field(None, alias="detail")
    code: str | None = Field(None, alias="code")
    request_id: str | None = Field(None, alias="requestId")
    origin: str | None = Field(None, alias="origin")
    status: str | None = Field(None, alias="status")
    status_text: str | None = Field(None, alias="statusText")
    timestamp: str | None = Field(None, alias="timestamp")
