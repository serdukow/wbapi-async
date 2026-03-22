from pydantic import Field

from ...types.base import BaseType


class BrandsItem(BaseType):
    """Brands"""

    id: int = Field()
    logo_url: str = Field(alias="logoUrl")
    name: str = Field()
