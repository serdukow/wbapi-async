from pydantic import Field

from ...types.base import BaseType
from .api_b2b_client_info import ApiB2BClientInfo
from .errors_item import ErrorsItem


class B2BBuyerInformationItem(BaseType):
    """B2B Buyer Information"""

    data: ApiB2BClientInfo | None = Field(None, alias="data")
    errors: list[ErrorsItem] | None = Field(None, alias="errors")
    is_error: bool = Field(alias="isError")
    order_id: int = Field(alias="orderId")
