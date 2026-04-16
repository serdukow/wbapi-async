from pydantic import Field

from ...types.base import BaseType


class CustomsDeclaration(BaseType):
    """Customs declaration number"""

    value: str | None = Field(None)
