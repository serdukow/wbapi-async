from pydantic import Field

from ...types.base import BaseType
from .supplier_task_metadata import SupplierTaskMetadata


class ProcessedUploadStateResponse(BaseType):
    """Processed Upload State"""

    data: SupplierTaskMetadata | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
