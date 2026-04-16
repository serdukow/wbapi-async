from pydantic import Field

from ...types.base import BaseType
from .data_4 import Data4


class DocumentsResponse(BaseType):
    """Get Documents"""

    data: Data4 | None = Field(None, alias="data")
