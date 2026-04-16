from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AssemblyOrdersMetadataItem(BaseType):
    """Get Assembly Orders Metadata"""

    id_: int | None = Field(None, alias="id")
    meta_details: list[dict[str, Any]] | None = Field(None, alias="metaDetails")
    meta: dict[str, Any] | None = Field(None)
