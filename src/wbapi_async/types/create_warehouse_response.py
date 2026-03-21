from pydantic import Field

from .base import BaseType


class CreateWarehouseResponse(BaseType):
    """Create Warehouse"""

    id: int | None = Field(None)
