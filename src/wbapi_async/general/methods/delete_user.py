from pydantic import Field

from ...methods.base import WbMethod
from ...types import DeleteUserResponse, RequestLimit


class DeleteUser(WbMethod):
    """
    Method is available by Personal token

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1user/delete
    """

    __return__ = DeleteUserResponse
    __empty_response__ = True
    __api__ = "user-management-api"
    __method__ = "api/v1/user"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    deleted_user_id: int = Field(alias="deletedUserID")
