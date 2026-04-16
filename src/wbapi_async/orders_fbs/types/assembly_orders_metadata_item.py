from pydantic import Field

from ...types.base import BaseType
from .meta import Meta


class AssemblyOrdersMetadataItem(BaseType):
    """Get Assembly Orders Metadata"""

    id_: int | None = Field(None, alias="id")
    meta: Meta | None = Field(None)
