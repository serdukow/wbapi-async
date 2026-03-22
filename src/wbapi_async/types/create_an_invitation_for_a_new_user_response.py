from pydantic import Field

from .base import BaseType


class CreateAnInvitationForANewUserResponse(BaseType):
    """Create an Invitation for a New User"""

    invite_id: str = Field(None, alias="inviteID")
    expired_at: str = Field(None, alias="expiredAt")
    is_success: bool = Field(None, alias="isSuccess")
    invite_url: str = Field(None, alias="inviteUrl")
