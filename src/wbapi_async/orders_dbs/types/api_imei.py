from pydantic import Field

from ...types.base import BaseType


class ApiImei(BaseType):
    order_id: int | None = Field(None, alias="orderId")
    imei: str | None = Field(None, alias="imei")
