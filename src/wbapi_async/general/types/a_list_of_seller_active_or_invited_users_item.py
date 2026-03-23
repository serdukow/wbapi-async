from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AListOfSellerActiveOrInvitedUsersItem(BaseType):
    """Get a List of Seller Active or Invited Users"""

    id_: int = Field(alias="id")
    role: str = Field()
    position: str = Field()
    phone: str = Field()
    email: str = Field()
    is_owner: bool = Field(alias="isOwner")
    first_name: str = Field(alias="firstName")
    second_name: str = Field(alias="secondName")
    patronymic: str = Field()
    goods_return: bool = Field(alias="goodsReturn")
    is_invitee: bool = Field(alias="isInvitee")
    invitee_info: dict[str, Any] | None = Field(None, alias="inviteeInfo")
    access: list[dict[str, Any]] = Field()
