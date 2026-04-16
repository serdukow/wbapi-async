from pydantic import Field

from ...types.base import BaseType
from .imei import Imei


class Meta(BaseType):
    """Assembly order metadata"""

    imei: Imei | None = Field(None)
    uin: Imei | None = Field(None)
    gtin: Imei | None = Field(None)
    sgtin: Imei | None = Field(None)
    expiration: Imei | None = Field(None)
    customs_declaration: Imei | None = Field(None, alias="customsDeclaration")
