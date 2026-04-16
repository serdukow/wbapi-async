from pydantic import Field

from ...types.base import BaseType
from .supplier_task_metadata import SupplierTaskMetadata


class ProcessedUploadStateResponse(BaseType):
    """Processed Upload State"""

    data: SupplierTaskMetadata | None = Field(None, alias="data")
    error: bool | None = Field(None, alias="error")
    error_text: str | None = Field(None, alias="errorText")
