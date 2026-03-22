from pydantic import Field

from ...methods.base import WbMethod
from ...types import AListOfSellerActiveOrInvitedUsersItem, RequestLimit


class GetAListOfSellerActiveOrInvitedUsers(WbMethod):
    """
    Method is available by Personal token

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1users/get
    """

    __return__ = AListOfSellerActiveOrInvitedUsersItem
    __api__ = "user-management-api"
    __method__ = "api/v1/users"
    __data_key__ = "users"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int | None = Field(100)
    offset: int | None = Field(0)
    is_invite_only: bool | None = Field(False, alias="isInviteOnly")
