from pydantic import Field

from ...types.base import BaseType
from .api_meta_error_response import ApiMetaErrorResponse


class AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem(BaseType):
    """Add Data Matrix Codes to the Assembly Orders (Chestny ZNAK)"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[ApiMetaErrorResponse] | None = Field(None)
