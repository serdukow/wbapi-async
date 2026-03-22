from typing import Any

from pydantic import Field

from .base import BaseType


class AListOfSellerActiveOrInvitedUsersItem(BaseType):
    """Get a List of Seller Active or Invited Users"""

    id: int = Field(None)
    role: str = Field(None)
    position: str = Field(None)
    phone: str = Field(None)
    email: str = Field(None)
    is_owner: bool = Field(None, alias="isOwner")
    first_name: str = Field(None, alias="firstName")
    second_name: str = Field(None, alias="secondName")
    patronymic: str = Field(None)
    goods_return: bool = Field(None, alias="goodsReturn")
    is_invitee: bool = Field(None, alias="isInvitee")
    invitee_info: dict[str, Any] | None = Field(None, alias="inviteeInfo")
    access: list[dict[str, Any]] = Field(None)
