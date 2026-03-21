from pydantic import Field

from ..types.create_a_tag_response import CreateATagResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreateATag(WbMethod):
    """
    Creates a tag.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag/post
    """

    __return__ = CreateATagResponse
    __api__ = "content-api"
    __method__ = "content/v2/tag"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    color: str | None = Field(None)
    name: str | None = Field(None)
