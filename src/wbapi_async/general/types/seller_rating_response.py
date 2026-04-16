from pydantic import Field

from ...types.base import BaseType


class SellerRatingResponse(BaseType):
    """Get Seller Rating"""

    feedback_count: int | None = Field(None, alias="feedbackCount")
    valuation: float | None = Field(None)
