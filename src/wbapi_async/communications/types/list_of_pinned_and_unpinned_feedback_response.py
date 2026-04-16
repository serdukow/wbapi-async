from typing import Any

from pydantic import Field

from ...types.base import BaseType


class ListOfPinnedAndUnpinnedFeedbackResponse(BaseType):
    """List of Pinned and Unpinned Feedback"""

    data: dict[str, Any] = Field()
    next_: int | None = Field(None, alias="next")
