from pydantic import Field

from ...types.base import BaseType
from .supplier_task_metadata_buffer import SupplierTaskMetadataBuffer


class UnprocessedUploadStateResponse(BaseType):
    """Unprocessed Upload State"""

    data: SupplierTaskMetadataBuffer | None = Field(None, alias="data")
    error: bool | None = Field(None, alias="error")
    error_text: str | None = Field(None, alias="errorText")
