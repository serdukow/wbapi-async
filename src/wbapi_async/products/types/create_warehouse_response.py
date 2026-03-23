from pydantic import Field

from ...types.base import BaseType


class CreateWarehouseResponse(BaseType):
    """Create Warehouse"""

    id_: int | None = Field(None, alias="id")
