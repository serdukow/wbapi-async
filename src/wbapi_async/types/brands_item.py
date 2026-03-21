from pydantic import Field

from .base import BaseType


class BrandsItem(BaseType):
    """Brands"""

    id: int = Field(None)
    logo_url: str = Field(None, alias="logoUrl")
    name: str = Field(None)
