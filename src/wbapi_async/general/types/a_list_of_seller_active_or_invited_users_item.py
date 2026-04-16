from pydantic import Field

from ...types.base import BaseType
from ..enums.role import Role
from .access_item import AccessItem
from .invitee_info import InviteeInfo


class AListOfSellerActiveOrInvitedUsersItem(BaseType):
    """Get a List of Seller Active or Invited Users"""

    id_: int = Field(alias="id")
    role: Role = Field()
    position: str = Field()
    phone: str = Field()
    email: str = Field()
    is_owner: bool = Field(alias="isOwner")
    first_name: str = Field(alias="firstName")
    second_name: str = Field(alias="secondName")
    patronymic: str = Field()
    goods_return: bool = Field(alias="goodsReturn")
    is_invitee: bool = Field(alias="isInvitee")
    invitee_info: InviteeInfo | None = Field(None, alias="inviteeInfo")
    access: list[AccessItem] = Field()
