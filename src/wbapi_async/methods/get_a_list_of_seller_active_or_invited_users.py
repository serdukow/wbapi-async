from pydantic import Field

from ..types.a_list_of_seller_active_or_invited_users_item import AListOfSellerActiveOrInvitedUsersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetAListOfSellerActiveOrInvitedUsers(WbMethod):
    """
    <div class="description_token">

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1users/get
    """

    __return__ = AListOfSellerActiveOrInvitedUsersItem
    __api__ = "user-management-api"
    __method__ = "api/v1/users"
    __data_key__ = "users"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=5)

    limit: int | None = Field(100)
    offset: int | None = Field(0)
    is_invite_only: bool | None = Field(False, alias="isInviteOnly")
