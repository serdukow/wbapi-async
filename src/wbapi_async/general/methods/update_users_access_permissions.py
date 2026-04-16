from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, UpdateUsersAccessPermissionsResponse, UserAccess


class UpdateUsersAccessPermissions(WbMethod):
    """
    Method is available by Personal token

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1users~1access/put
    """

    __return__ = UpdateUsersAccessPermissionsResponse
    __empty_response__ = True
    __api__ = "user-management-api"
    __method__ = "api/v1/users/access"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    users_accesses: list[UserAccess] = Field(alias="usersAccesses")
