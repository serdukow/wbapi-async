from typing import Any

from pydantic import Field

from ...types.base import BaseType


class PinnedFeedbackLimitsResponse(BaseType):
    """Pinned Feedback Limits"""

    data: dict[str, Any] = Field(alias="data")
