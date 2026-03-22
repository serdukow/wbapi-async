from pydantic import Field

from ...types.base import BaseType


class CheckIfTheOrderBelongsToTheBuyerResponse(BaseType):
    """Check If the Order Belongs to the Buyer"""

    ok: bool | None = Field(None)
