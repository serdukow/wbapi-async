from ...methods.base import WbMethod
from ...types import RequestLimit, TagsListResponse


class GetTagsList(WbMethod):
    """
    Returns seller's tags list

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tags/get
    """

    __return__ = TagsListResponse
    __api__ = "content-api"
    __method__ = "content/v2/tags"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
