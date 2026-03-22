from typing import Any

from pydantic import Field

from ...types.base import BaseType


class CourierInfoItem(BaseType):
    """Courier Info"""

    courier_info: dict[str, Any] | None = Field(None, alias="courierInfo")
    order_id: int | None = Field(None, alias="orderID")
