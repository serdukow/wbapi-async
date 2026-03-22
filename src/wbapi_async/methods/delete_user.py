from pydantic import Field

from ..types.delete_user_response import DeleteUserResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteUser(WbMethod):
    """
    <div class="description_token">

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1user/delete
    """

    __return__ = DeleteUserResponse
    __empty_response__ = True
    __api__ = "user-management-api"
    __method__ = "api/v1/user"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=10)

    deleted_user_id: int = Field(None, alias="deletedUserID")
