from pydantic import Field

from ...types.base import BaseType


class JamSubscriptionInformationResponse(BaseType):
    """Get Jam Subscription Information"""

    state: str = Field()
    activation_source: str = Field(alias="activationSource")
    level: str = Field()
    since: str = Field()
    till: str = Field()
