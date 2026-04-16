from pydantic import Field

from ...types.base import BaseType
from .errors_item import ErrorsItem


class NotifyThatTheOrdersAreReceivedItem(BaseType):
    """Notify that the Orders Are Received"""

    errors: list[ErrorsItem] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
