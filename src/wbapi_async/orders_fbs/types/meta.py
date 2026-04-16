from pydantic import Field

from ...types.base import BaseType
from .imei import Imei


class Meta(BaseType):
    """Assembly order metadata"""

    imei: Imei | None = Field(None, alias="imei")
    uin: Imei | None = Field(None, alias="uin")
    gtin: Imei | None = Field(None, alias="gtin")
    sgtin: Imei | None = Field(None, alias="sgtin")
    expiration: Imei | None = Field(None, alias="expiration")
    customs_declaration: Imei | None = Field(None, alias="customsDeclaration")
