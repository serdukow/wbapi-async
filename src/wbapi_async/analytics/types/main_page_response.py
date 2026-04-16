from typing import Any

from pydantic import Field

from ...types.base import BaseType


class MainPageResponse(BaseType):
    """Main Page"""

    data: dict[str, Any] = Field()
