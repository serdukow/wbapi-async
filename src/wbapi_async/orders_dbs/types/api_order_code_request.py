from pydantic import Field

from ...types.base import BaseType


class ApiOrderCodeRequest(BaseType):
    code: str | None = Field(None, alias="code")
    order_id: int | None = Field(None, alias="orderId")
