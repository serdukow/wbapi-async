from pydantic import Field

from ...products.types.data import Data
from ...types.base import BaseType


class DocumentResponse(BaseType):
    """Get Document"""

    data: Data | None = Field(None)
