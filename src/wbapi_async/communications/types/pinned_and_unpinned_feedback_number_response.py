from typing import Any

from pydantic import Field

from ...types.base import BaseType


class PinnedAndUnpinnedFeedbackNumberResponse(BaseType):
    """Pinned and Unpinned Feedback Number"""

    data: dict[str, Any] = Field(alias="data")
