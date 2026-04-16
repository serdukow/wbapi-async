from pydantic import Field

from ...types.base import BaseType


class ParamsItem(BaseType):
    extension: str | None = Field(None)
    service_name: str | None = Field(None, alias="serviceName")
