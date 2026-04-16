from pydantic import Field

from ...products.types.data import Data
from ...types.base import BaseType


class DocumentsResponse(BaseType):
    """Get Documents"""

    data: Data | None = Field(None)
