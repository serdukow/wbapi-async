from pydantic import Field

from ...types.base import BaseType


class ApiUin(BaseType):
    order_id: int | None = Field(None, alias="orderId")
    uin: str | None = Field(None, alias="uin")
