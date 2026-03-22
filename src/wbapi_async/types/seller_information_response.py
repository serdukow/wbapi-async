from pydantic import Field

from .base import BaseType


class SellerInformationResponse(BaseType):
    """Get Seller Information"""

    name: str | None = Field(None)
    sid: str | None = Field(None)
    tin: str | None = Field(None)
    trade_mark: str | None = Field(None, alias="tradeMark")
