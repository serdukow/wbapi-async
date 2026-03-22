from pydantic import Field

from ...types.base import BaseType


class TheFeedbackByIdItem(BaseType):
    """Get the Feedback by ID"""

    full_size: str | None = Field(None, alias="fullSize")
    mini_size: str | None = Field(None, alias="miniSize")
