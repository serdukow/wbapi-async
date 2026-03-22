from pydantic import Field

from .base import BaseType


class CampaignBudgetResponse(BaseType):
    """Campaign Budget"""

    cash: int | None = Field(None)
    netting: int | None = Field(None)
    total: int | None = Field(None)
