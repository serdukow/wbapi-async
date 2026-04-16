from pydantic import Field

from ...types.base import BaseType


class InviteeInfo(BaseType):
    """Invitation information, if the user is invited"""

    phone_number: str | None = Field(None, alias="phoneNumber")
    position: str | None = Field(None, alias="position")
    invite_uuid: str | None = Field(None, alias="inviteUuid")
    expired_at: str | None = Field(None, alias="expiredAt")
    is_active: bool | None = Field(None, alias="isActive")
