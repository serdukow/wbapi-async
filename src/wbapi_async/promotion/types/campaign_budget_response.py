from pydantic import Field

from ...types.base import BaseType


class CampaignBudgetResponse(BaseType):
    """Campaign Budget"""

    cash: int | None = Field(None, alias="cash")
    netting: int | None = Field(None, alias="netting")
    total: int | None = Field(None, alias="total")
