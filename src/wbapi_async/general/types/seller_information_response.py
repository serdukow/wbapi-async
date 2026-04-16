from pydantic import Field

from ...types.base import BaseType


class SellerInformationResponse(BaseType):
    """Get Seller Information"""

    name: str | None = Field(None, alias="name")
    sid: str | None = Field(None, alias="sid")
    tin: str | None = Field(None, alias="tin")
    trade_mark: str | None = Field(None, alias="tradeMark")
