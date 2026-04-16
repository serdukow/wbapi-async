from pydantic import Field

from ...types.base import BaseType


class ApiSgtiNs(BaseType):
    order_id: int | None = Field(None, alias="orderId")
    sgtins: list[str] | None = Field(None, alias="sgtins")
