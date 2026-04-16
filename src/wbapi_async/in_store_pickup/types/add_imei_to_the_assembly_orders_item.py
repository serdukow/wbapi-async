from pydantic import Field

from ...types.base import BaseType
from .api_meta_error_response import ApiMetaErrorResponse


class AddImeiToTheAssemblyOrdersItem(BaseType):
    """Add IMEI to the Assembly Orders"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[ApiMetaErrorResponse] | None = Field(None, alias="errors")
