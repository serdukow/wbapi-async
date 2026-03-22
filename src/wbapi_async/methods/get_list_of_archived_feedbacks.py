from pydantic import Field

from ..types.list_of_archived_feedbacks_item import ListOfArchivedFeedbacksItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetListOfArchivedFeedbacks(WbMethod):
    """
    The method allows you to get a list of archived feedbacks. <br>

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1archive/get
    """

    __return__ = ListOfArchivedFeedbacksItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/archive"
    __data_key__ = "data.feedbacks"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    nm_id: int | None = Field(None, alias="nmId")
    take: int = Field(None)
    skip: int = Field(None)
    order: str | None = Field(None)
