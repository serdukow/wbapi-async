from pydantic import Field

from ...types.base import BaseType


class BrandsItem(BaseType):
    """Brands"""

    id_: int = Field(alias="id")
    logo_url: str = Field(alias="logoUrl")
    name: str = Field(alias="name")
