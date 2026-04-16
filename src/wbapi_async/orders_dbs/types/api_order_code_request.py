from pydantic import Field

from ...types.base import BaseType


class ApiOrderCodeRequest(BaseType):
    code: str | None = Field(None)
    order_id: int | None = Field(None, alias="orderId")
