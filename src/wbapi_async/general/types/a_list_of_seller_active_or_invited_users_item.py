from pydantic import Field

from ...types.base import BaseType
from .access_item import AccessItem
from .invitee_info import InviteeInfo


class AListOfSellerActiveOrInvitedUsersItem(BaseType):
    """Get a List of Seller Active or Invited Users"""

    id_: int = Field(alias="id")
    role: str = Field(alias="role")
    position: str = Field(alias="position")
    phone: str = Field(alias="phone")
    email: str = Field(alias="email")
    is_owner: bool = Field(alias="isOwner")
    first_name: str = Field(alias="firstName")
    second_name: str = Field(alias="secondName")
    patronymic: str = Field(alias="patronymic")
    goods_return: bool = Field(alias="goodsReturn")
    is_invitee: bool = Field(alias="isInvitee")
    invitee_info: InviteeInfo | None = Field(None, alias="inviteeInfo")
    access: list[AccessItem] = Field(alias="access")
