from pydantic import Field

from ...types.base import BaseType
from .courier_info import CourierInfo


class CourierInfoItem(BaseType):
    """Courier Info"""

    courier_info: CourierInfo | None = Field(None, alias="courierInfo")
    order_id: int | None = Field(None, alias="orderID")
