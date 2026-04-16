from pydantic import Field

from ...types.base import BaseType


class ApiGtin(BaseType):
    gtin: str | None = Field(None)
    order_id: int | None = Field(None, alias="orderId")
