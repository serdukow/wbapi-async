from pydantic import Field

from ...types import CreateATagResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class CreateATag(WbMethod):
    """
    Creates a tag.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag/post
    """

    __return__ = CreateATagResponse
    __api__ = "content-api"
    __method__ = "content/v2/tag"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    color: str | None = Field(None)
    name: str | None = Field(None)
