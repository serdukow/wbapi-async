from ..types.request_limit import RequestLimit
from ..types.tags_list_response import TagsListResponse
from .base import WbMethod


class TagsList(WbMethod):
    """
    Tags List

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tags/get
    """

    __return__ = TagsListResponse
    __api__ = "content-api"
    __method__ = "content/v2/tags"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)
