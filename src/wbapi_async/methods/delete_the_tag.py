from pydantic import Field

from ..types.delete_the_tag_response import DeleteTheTagResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteTheTag(WbMethod):
    """
    Deletes the tag

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1%7Bid%7D/delete
    """

    __return__ = DeleteTheTagResponse
    __api__ = "content-api"
    __method__ = ""
    __method_template__ = "content/v2/tag/{id}"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    id: int = Field(exclude=True)
