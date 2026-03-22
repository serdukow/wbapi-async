from pydantic import Field

from ...types.base import BaseType


class CreateWarehouseResponse(BaseType):
    """Create Warehouse"""

    id: int | None = Field(None)
