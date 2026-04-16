from pydantic import Field

from ...types.base import BaseType
from .supplier_task_metadata_buffer import SupplierTaskMetadataBuffer


class UnprocessedUploadStateResponse(BaseType):
    """Unprocessed Upload State"""

    data: SupplierTaskMetadataBuffer | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
