from typing import Any

from pydantic import Field

from ..types.update_users_access_permissions_response import UpdateUsersAccessPermissionsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class UpdateUsersAccessPermissions(WbMethod):
    """
    <div class="description_token">

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1users~1access/put
    """

    __return__ = UpdateUsersAccessPermissionsResponse
    __empty_response__ = True
    __api__ = "user-management-api"
    __method__ = "api/v1/users/access"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=5)

    users_accesses: list[Any] = Field(None, alias="usersAccesses")
