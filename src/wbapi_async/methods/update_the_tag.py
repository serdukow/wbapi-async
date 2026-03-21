from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.update_the_tag_response import UpdateTheTagResponse
from .base import WbMethod


class UpdateTheTag(WbMethod):
    """
    Update the Tag

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1%7Bid%7D/patch
    """

    __return__ = UpdateTheTagResponse
    __api__ = "content-api"
    __method__ = ""
    __method_template__ = "content/v2/tag/{id}"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    id: int = Field(exclude=True)
    color: str | None = Field(None)
    name: str | None = Field(None)
