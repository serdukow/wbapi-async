from typing import Any

from pydantic import Field

from ...types.base import BaseType


class UnpinFeedbackResponse(BaseType):
    """Unpin Feedback"""

    data: dict[str, Any] = Field(alias="data")
