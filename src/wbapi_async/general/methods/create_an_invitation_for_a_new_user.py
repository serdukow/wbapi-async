from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import CreateAnInvitationForANewUserResponse, RequestLimit


class CreateAnInvitationForANewUser(WbMethod):
    """
    Method is available by Personal token

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1invite/post
    """

    __return__ = CreateAnInvitationForANewUserResponse
    __api__ = "user-management-api"
    __method__ = "api/v1/invite"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    access: list[dict[str, Any]] | None = Field(None)
    invite: dict[str, Any] = Field()
