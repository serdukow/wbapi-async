from typing import Any

from pydantic import Field

from ..types.create_an_invitation_for_a_new_user_response import CreateAnInvitationForANewUserResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreateAnInvitationForANewUser(WbMethod):
    """
    <div class="description_token">

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1invite/post
    """

    __return__ = CreateAnInvitationForANewUserResponse
    __api__ = "user-management-api"
    __method__ = "api/v1/invite"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=5)

    access: list[dict[str, Any]] | None = Field(None)
    invite: dict[str, Any] = Field(None)
