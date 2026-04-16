from pydantic import Field

from ...types.base import BaseType
from .customs_declaration import CustomsDeclaration
from .expiration import Expiration
from .gtin import Gtin
from .imei import Imei
from .sgtin import Sgtin
from .uin import Uin


class Meta(BaseType):
    """Assembly order metadata"""

    imei: Imei | None = Field(None)
    uin: Uin | None = Field(None)
    gtin: Gtin | None = Field(None)
    sgtin: Sgtin | None = Field(None)
    expiration: Expiration | None = Field(None)
    customs_declaration: CustomsDeclaration | None = Field(None, alias="customsDeclaration")
