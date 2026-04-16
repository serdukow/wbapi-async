from pydantic import Field

from ...types.base import BaseType
from .models_good_in_box import ModelsGoodInBox


class SupplyPackageResponse(BaseType):
    """Supply Package"""

    package_code: str | None = Field(None, alias="packageCode")
    quantity: int | None = Field(None, alias="quantity")
    barcodes: list[ModelsGoodInBox] | None = Field(None, alias="barcodes")
