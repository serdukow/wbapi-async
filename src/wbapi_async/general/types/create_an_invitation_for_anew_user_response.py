from pydantic import Field

from ...types.base import BaseType


class CreateAnInvitationForANewUserResponse(BaseType):
    """Create an Invitation for a New User"""

    invite_id: str = Field(alias="inviteID")
    expired_at: str = Field(alias="expiredAt")
    is_success: bool = Field(alias="isSuccess")
    invite_url: str = Field(alias="inviteUrl")
